from django.conf.urls import url, include

from viewflow.flow.viewset import FlowViewSet

from .flows import MayorOrdinanceFlow, MayorInstructionFlow

urlpatterns = [
    url(r'^mayor_ordinance/', include(FlowViewSet(MayorOrdinanceFlow).urls, namespace='mayor_ordinance')),
    url(r'^mayor_instruction/', include(FlowViewSet(MayorInstructionFlow).urls, namespace='mayor_instruction')),

]
