from django import forms
from django.forms.models import inlineformset_factory
from .models import Document, DocumentSubscriber, DocumentExecutor, Attachment


class CreateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['date_created', 'status', 'created_by']


class UpdateDocumentForm(forms.ModelForm):
    go_to_next_stage = forms.BooleanField(required=False)

    class Meta:
        model = Document
        exclude = ['date_created', 'status', ]


AttachmentFormSet = inlineformset_factory(Document, Attachment, exclude=[], extra=1)
SubscriberFormSet = inlineformset_factory(Document, DocumentSubscriber, extra=1,
                                          exclude=['viewed'], labels={'employee': 'Працівник'})
ExecutorFormSet = inlineformset_factory(Document, DocumentExecutor, extra=1,
                                        exclude=['executed'], labels={'employee': 'Працівник'}, )
