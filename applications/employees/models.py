from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models.signals import post_save
from django.db import models
from django.core.mail import send_mail
from django.core import validators
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .managers import TemporalQuerySet

from system.email_sender import send_letter

# from documents.models.base import DocumentMeta


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user realization based on Django AbstractUser and PermissionMixin.
    """
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': "Користувач з такою електронною поштою вже існує",
                              })

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    middle_name = models.CharField(max_length=64, verbose_name='по батькові')

    phone = models.CharField(max_length=64, verbose_name=_('user phone'))

    # system field
    username = models.CharField(_('username'), max_length=30,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',
                                                              _('Enter a valid username. '
                                                                'This value may contain only letters, numbers '
                                                                'and @/./+/-/_ characters.'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with that username already exists."),
                                })
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    objects = UserManager()

    signed_on_notifications = models.BooleanField(default=True, verbose_name="Підписаний на сповіщення")
    # this stuff is needed to use this model with django auth as a custom user class
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        """
        Generates user full name.
        Returns:
            The first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_initials(self):
        """
        Показываем полные инициалы: П.В.С
        """

        firstname = '.'.join(name[0].upper() for name in self.first_name.split())
        midlename = '.'.join(name[0].upper() for name in self.middle_name.split())
        full_name = '%s %s.%s.' % (self.last_name, firstname, midlename)
        return full_name.strip()

    def get_short_name(self):
        """
        Generates user short name.
        Returns:
            The short name for the user
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + (' ' + self.middle_name if self.middle_name else '')

    class Meta:
        managed = True
        abstract = False
        db_table = 'auth_user'
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def get_list(self, model_class):
        return model_class.objects.filter(user=self)

    # def count_inbox_documents(self):
    #     employee = DeptEmp.objects.filter(employee=self).first()
    #     count = DocumentMeta.objects.filter(status='approving', officememo__officememo_approvers__employee=employee,
    #                                         officememo__officememo_approvers__answered=False).count()
    #     return count


class Department(models.Model):
    dept_no = models.CharField(_('code'), primary_key=True, max_length=25)
    dept_name = models.CharField(_('name'), unique=True, max_length=150)

    class Meta:
        verbose_name = _('department')
        verbose_name_plural = _('departments')
        db_table = 'departments'
        ordering = ['dept_no']

    def __str__(self):
        return self.dept_name


class DeptEmp(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))
    from_date = models.DateField(_('from'))
    to_date = models.DateField(_('to'))

    objects = TemporalQuerySet.as_manager()

    class Meta:
        verbose_name = _('department employee')
        verbose_name_plural = _('department employees')
        db_table = 'dept_emp'
        unique_together = (('employee', 'department'),)


    def __str__(self):
        return "{} - {}".format(self.employee, self.department)


class DeptManager(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))
    from_date = models.DateField(_('from'))
    to_date = models.DateField(_('to'))

    objects = TemporalQuerySet.as_manager()

    class Meta:
        verbose_name = _('department manager')
        verbose_name_plural = _('department managers')
        db_table = 'dept_manager'
        ordering = ['-from_date']
        unique_together = (('employee', 'department'),)

    def __str__(self):
        return "{} - {}".format(self.employee, self.department)


class Title(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    title = models.CharField(_('title'), max_length=100)
    from_date = models.DateField(_('from'))
    to_date = models.DateField(_('to'), blank=True, null=True)

    objects = TemporalQuerySet.as_manager()

    class Meta:
        verbose_name = _('title')
        verbose_name_plural = _('titles')
        db_table = 'titles'

    def __str__(self):
        return "{} - {}".format(self.employee, self.title)


class ProxyGroup(Group):
    class Meta:
        proxy = True
        verbose_name = 'група'
        verbose_name_plural = 'групи'


@receiver(post_save, sender=User, dispatch_uid='DocFlow.employees.models.user_post_save_handler')
def post_save(sender, instance, created, **kwargs):
    if created:
        try:
            group, created = Group.objects.get_or_create(name='Користувачі')
            instance.groups.add(group)
        except:
            pass
        instance.is_active = False
        instance.save()

        admins_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))
        context = {
            'id': instance.id,
            'name': instance.get_full_name() or instance.username}
        subject = 'Зареєстрований новий користувач'
        template_name = 'new_user.email'
        send_letter(subject, template_name, context, admins_emails)
