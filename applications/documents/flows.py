from viewflow.base import Flow, this
from viewflow import flow

from . import views

from .models import DocumentProcess


class MayorOrdinanceFlow(Flow):
    process_class = DocumentProcess

    start = (
        flow.Start(views.MayorOrdinanceCreateView)
            .Next(this.document_update)
    )

    document_update = (
        flow.View(views.MayorOrdinanceUpdateView)
            .Assign(lambda activation: activation.process.get_owner())
            .Next(this.end)
    )

    go_to_next_stage = (
        flow.If(cond=lambda activation: activation.process.go_to_next_stage)
            .Then(this.end)
            .Else(this.document_update)
    )

    end = (
        flow.End()
    )


class MayorInstructionFlow(Flow):
    process_class = DocumentProcess

    start = (
        flow.Start(views.MayorInstructionCreateView)
            .Next(this.document_update)
    )

    document_update = (
        flow.View(views.MayorInstructionUpdateView)
            .Assign(lambda activation: activation.process.get_owner())
            .Next(this.end)
    )

    end = (
        flow.End()
    )
