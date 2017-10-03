from .base import Document, DocumentProcess, DocumentSubscriber, Attachment, DocumentExecutor
from .documents import InnerLetter, OuterLetter, CitizensAppeal, InformationRequest, MayorOrdinance, MayorInstruction, \
    MeetingProtocol, OfficeMemo

documents = ['InnerLetter', 'OuterLetter', 'CitizensAppeal', 'InformationRequest', 'MayorInstruction', 'MayorOrdinance',
             'MeetingProtocol', 'OfficeMemo']

base = ['Document', 'DocumentProcess', 'DocumentSubscriber', 'DocumentExecutor', 'Attachment']

__all__ = documents + base
