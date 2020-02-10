"""
Definition of urls for WebApp.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from Main import mviews
from Accounts import aviews

urlpatterns = [
    #############################
    ####Login & Registration#####
    #############################
    path('', include('django.contrib.auth.urls')),
    path('register/', aviews.register, name="register"),
    #############################
    #####Articles & Dashboard####
    #############################
    path('dashboard/', aviews.dashboard, name='dashboard'),
    path('dashboard/post/', aviews.post, name='post'),
    path('article/<slug:slug>/', mviews.article_dynamic, name='article_dynamic'),
    path('article/<slug:slug>/delete', mviews.article_delete, name='article_delete'),
    path('article/<slug:slug>/edit', mviews.article_edit, name='article_edit'),
    path('article/', mviews.article, name='article'),
    #############################
    ########Main Content#########
    #############################
    path('', mviews.home, name="home"),
    path('admin/', admin.site.urls),
]
