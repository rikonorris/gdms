"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.static import serve

from filemanager import path_end

from . import settings
from . import views

import debug_toolbar

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': False}),

    url(r'^filemanager/' + path_end, views.document_view, name='filemanager'),

    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/signup/$', views.register, name='register'),
    url(r'^documents_view/' + path_end, views.document_view, name='documents'),
    url(r'^area51/', admin.site.urls),
    url(r'^todo/', include('todo.urls')),
    url(r'^document/+(?P<document_id>[0-9]+)', views.document, name='document'),
    url(r'^profile/+(?P<user_id>[0-9]+)', views.profile, name='profile'),

    url(r'^filer/', include('filer.urls')),

    # url(r'^my_documents/', views.my_documents, name='my_documents'),
    # url(r'^all-documents/', views.all_document_list, name='all_documents'),


    url(r'^inbox/', views.InboxDocumentListView.as_view(), name='inbox'),
    url(r'^drafts/', views.DraftListView.as_view(), name='drafts'),

    url(r'^create_document/', views.available_documents_type, name='create_document'),

    # Todo: delete after testing
    url(r'^$', views.available_documents_type, name='create_document'),


    url(r'^documents/', include('documents.urls', namespace='documents')),

    url(r'^__debug__/', include(debug_toolbar.urls)),

    url(r'^archive/', views.archive, name='archive'),
    url(r'^sent/', views.sent_documents, name='sent_documents'),
    url(r'^help/', views.help, name='help'),
    url(r'^notifications_subscribe/', views.notifications_subscription, name='notifications_subscription'),
    url(r'^search/', include('haystack.urls')),
]
