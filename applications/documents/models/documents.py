from django.db import models


# TODO: remove static methods if it will be described in views

class InnerLetter(models.Model):
    # control card ?
    page_number = models.PositiveIntegerField()

    @staticmethod
    def is_executors_required():
        return True

    @staticmethod
    def is_subscribers_required():
        return False


class OuterLetter(models.Model):
    page_number = models.PositiveIntegerField()
    # additional fields


class InformationRequest(models.Model):
    # control card ?

    @staticmethod
    def is_executors_required():
        return True

    @staticmethod
    def is_subscribers_required():
        return False


class CitizensAppeal(models.Model):
    # control card ?

    @staticmethod
    def is_executors_required():
        return True

    @staticmethod
    def is_subscribers_required():
        return False


class MayorOrdinance(models.Model):
    page_number = models.PositiveIntegerField()

    @staticmethod
    def is_executors_required():
        return False

    @staticmethod
    def is_subscribers_required():
        return False


class MayorInstruction(models.Model):
    page_number = models.PositiveIntegerField()

    @staticmethod
    def is_executors_required():
        return True

    @staticmethod
    def is_subscribers_required():
        return False


class MeetingProtocol(models.Model):
    page_number = models.PositiveIntegerField()

    @staticmethod
    def is_executors_required():
        return True

    @staticmethod
    def is_subscribers_required():
        return True


class OfficeMemo(models.Model):
    page_number = models.PositiveIntegerField()
    is_executors_required = models.BooleanField(default=True)
    is_subscribers_required = models.BooleanField(default=False)

    @staticmethod
    def is_executors_required():
        return True

    @staticmethod
    def is_subscribers_required():
        return False

# DOCUMENT_TYPES = (
#     ('InnerLetter', 'Вхідний лист'),
#     ('CitizensAppeal', 'Звернення громадян'),
#     ('InformationRequest', 'Запит на інформацію'),
#     ('OuterLetter', 'Вихідний лист'),
#     ('DraftDecision', 'Проект рішення'),
#     ('MayorOrdinance', 'Розпорядження міського голови'),
#     ('MayorInstruction', 'Доручення міського голови'),
#     ('MeetingProtocol', 'Протокол засідань'),
#     ('OfficeMemo', 'Службова записка'),
# )
