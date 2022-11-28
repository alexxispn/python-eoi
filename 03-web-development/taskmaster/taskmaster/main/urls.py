"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', views.home, name='home'),
    path('tasks/home', views.home, name='home'),
    path('tasks/high', views.high, name='high'),
    path('tasks/medium', views.medium, name='medium'),
    path('tasks/low', views.low, name='low'),
    path('tasks/finished', views.finished, name='finished'),
    path('tasks/unfinished', views.unfinished, name='unfinished'),
    path('tasks/projects/', views.projects, name='projects'),
    path('tasks/projects/<int:pk>/', views.project, name='project'),
    path('tasks/projects/<str:code>/', views.project_code, name='project_code'),
]
