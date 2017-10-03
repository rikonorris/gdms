from django.views import generic
from django.shortcuts import HttpResponseRedirect, render
from viewflow.flow.views import FlowMixin, StartFlowMixin

from . import forms
# from .mixins import


class DocumentCreateView(StartFlowMixin, generic.CreateView):
    form_class = forms.CreateDocumentForm
    template_name = "documents/document_create.html"

    def activation_done(self, *args, **kwargs):
        document = self.object
        document.created_by = self.request.user
        document.status = 'draft'
        document.save()
        self.activation.process.document = document
        super(DocumentCreateView, self).activation_done()


# mayor ordinance views
class MayorOrdinanceCreateView(DocumentCreateView):
    pass


class MayorOrdinanceUpdateView(FlowMixin, generic.View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# mayor instruction views
class MayorInstructionCreateView(DocumentCreateView):
    pass


class MayorInstructionUpdateView(FlowMixin, generic.View):
    pass

