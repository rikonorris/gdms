from datetime import datetime

from django.db import models

from viewflow.models import Process

from employees.models import DeptEmp
from system import settings

TYPE_CHOICES = (
    ('inner', 'Внутрішній'),
    ('outer', 'Зовнішній'),
)


class Document(models.Model):
    date_created = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=512)
    registration_number = models.CharField(unique=True, max_length=20)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)


class DocumentExecutor(models.Model):
    document = models.ForeignKey(Document)
    employee = models.ForeignKey(DeptEmp)
    executed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('document', 'employee')


class DocumentSubscriber(models.Model):
    document = models.ForeignKey(Document)
    employee = models.ForeignKey(DeptEmp)
    viewed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('document', 'employee')


class Attachment(models.Model):
    document = models.ForeignKey(Document)
    file = models.FileField(upload_to='files', default='')


class DocumentProcess(Process):
    document = models.ForeignKey(Document)
    go_to_next_stage = models.BooleanField(default=False)

    def get_owner(self):
        return self.document.created_by
