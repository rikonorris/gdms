from django.apps import AppConfig

from django.utils.translation import ugettext_lazy as _


class DocumentsConfig(AppConfig):
    name = 'documents'
    verbose_name = _('Documents')
