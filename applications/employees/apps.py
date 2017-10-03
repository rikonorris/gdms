from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from material.frontend.apps import ModuleMixin


class EmployeesConfig(ModuleMixin, AppConfig):
    name = 'employees'
    icon = '<i class="material-icons">people</i>'
    verbose_name = "Штатний розпис"

    def has_perm(self, user):
        return user.is_superuser
