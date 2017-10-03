import os
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import generic
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from pure_pagination.mixins import PaginationMixin

from documents.models import Document
from employees.models import DeptEmp
from todo.models import Item
from filemanager import FileManager

from .forms import SignupForm
from .settings import MEDIA_ROOT


# сторінка "Вхідні документи" вона ж дашборд
class InboxDocumentListView(PaginationMixin, generic.ListView):
    model = Document
    template_name = 'inbox.html'
    paginate_by = 10
    object = Document

    def get(self, request, *args, **kwargs):
        # create_calendar_events(self.request.user)
        return super(InboxDocumentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        valid_statuses = ['execution/familiarization', 'execution', 'familiarization']
        queryset = Document.objects.filter(
            Q(Q(documentexecutor__employee__employee=user, documentexecutor__executed=False) |
              Q(documentsubscriber__employee__employee=user, documentsubscriber__viewed=False)) &
            Q(status__in=valid_statuses)
        ).select_related('created_by')
        return queryset


# сторінка "Вихідні документи"
def sent_documents(request):
    return render(request, 'sent_documents.html')


# сторінка "Створити новий документ. Список доступних документів для створення"
def available_documents_type(request):
    return render(request, 'available_documents_type.html')


def document_view(request, path):
    fm = FileManager(os.path.join(MEDIA_ROOT, 'filemanager'), is_admin_view=True)
    return fm.render(request, path)


# сторінка "Мої документи"
# class myDocumentList(PaginationMixin, generic.ListView):
#     model = DocumentMeta
#     template_name = 'my_documents.html'
#     paginate_by = 10
#     object = DocumentMeta
#
#     def get_queryset(self):
#         queryset = DocumentMeta.objects.filter(status='approving',
#                                                created_by=self.request.user).exclude(status='draft')
#         return queryset


# my_documents = myDocumentList.as_view()


# def my_documents(request):
#     return render(request, 'my_documents.html')


# сторінка "Архівні документи"
def archive(request):
    return render(request, 'archive_documents.html')


# сторінка "Допомога"
def help(request):
    return render(request, 'help.html')


# сторінка "Чернетки"
class DraftListView(PaginationMixin, generic.ListView):
    model = Document
    template_name = 'drafts.html'
    paginate_by = 10
    object = Document

    def get_queryset(self):
        return Document.objects.filter(status='draft', created_by=self.request.user)


# сторінка "Звіти". Список звітів
# class AllDocumentsList(PaginationMixin, generic.ListView):
#     model = DocumentMeta
#     template_name = 'all_documents.html'
#     paginate_by = 10
#     object = DocumentMeta
#
#     def get_queryset(self):
#         user = self.request.user
#         employee = DeptEmp.objects.filter(employee=user).first()
#         queryset = DocumentMeta.objects.filter(
#             Q(status='approving',
#               officememo__officememo_approvers__employee=employee,
#               officememo__officememo_approvers__answered=False) |
#             Q(status='approving',
#               created_by=self.request.user)).order_by('date_created'). \
#             exclude(status='draft')
#         if self.request.GET.get('from'):
#             queryset = queryset.filter(date_created__gte=self.request.GET.get('from'))
#         if self.request.GET.get('to'):
#             queryset = queryset.filter(date_created__lte=self.request.GET.get('to'))
#         return queryset
#
#
# all_document_list = AllDocumentsList.as_view()


# картка документу
def document(request, document_id):
    return render(request, 'document.html')


# картка користувача
def profile(request, user_id):
    """
    показываем профиль пользователя
    :param request: HTTP request object
    :param user_id: User.id
    :return: Profile page for user with id=user_id
    """
    from employees.models import User
    if request.user.is_authenticated() and request.user.is_active:
        user = get_object_or_404(User, pk=user_id)
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('/accounts/login')


@csrf_exempt
def notifications_subscription(request):
    data = int(request.POST.get('value'))
    user = request.user
    user.signed_on_notifications = data
    user.save()
    return JsonResponse({'message': 'Was changed'}, safe=True)


def create_calendar_events(user):
    from django.urls import reverse
    task_list = Item.objects.filter(assigned_to=user.id, completed=False)
    result = []
    for task in task_list:
        if task.created_date <= task.due_date:
            url = reverse('todo-task_detail', kwargs={'task_id': task.id})
            result.append({
                "id": task.id,
                "name": task.title,
                "startdate": str(task.created_date),
                "enddate": str(task.due_date),
                "color": "#7AC29A",
                "url": url
            })
    monthly_result = {
        "monthly": result
    }
    json_result = json.dumps(monthly_result)
    with open('static/calendar/js/events.json', "w") as file:
        file.write(json_result)


def register(request):
    form = SignupForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

    context = {
        "form": form,
    }
    return render(request, 'registration/register.html', context)
