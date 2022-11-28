from django.shortcuts import render
from django.utils import timezone

from . import models


def home(request):
    date = timezone.now().date()
    tasks = models.Task.objects.all().order_by('name')
    return render(request, 'tasks/home.html', {'date': date, 'tasks': tasks})


def high(request):
    date = timezone.now().date()
    tasks = models.Task.objects.filter(priority='High').order_by('name')
    return render(request, 'tasks/high.html', {'date': date, 'tasks': tasks})


def medium(request):
    date = timezone.now().date()
    tasks = models.Task.objects.filter(priority='Medium').order_by('name')
    return render(request, 'tasks/medium.html', {'date': date, 'tasks': tasks})


def low(request):
    date = timezone.now().date()
    tasks = models.Task.objects.filter(priority='Low').order_by('name')
    return render(request, 'tasks/low.html', {'date': date, 'tasks': tasks})


def finished(request):
    date = timezone.now().date()
    tasks = models.Task.objects.filter(finished=True).order_by('name')
    return render(request, 'tasks/finished.html',
                  {'date': date, 'tasks': tasks})


def unfinished(request):
    date = timezone.now().date()
    tasks = models.Task.objects.filter(finished=False).order_by('name')
    return render(request, 'tasks/unfinished.html',
                  {'date': date, 'tasks': tasks})


def projects(request):
    projects = models.Project.objects.all()
    return render(request, 'tasks/projects.html', {'projects': projects})


def project(request, pk):
    project = models.Project.objects.get(pk=pk)
    return render(request, 'tasks/project.html',
                  {'project': project})


def project_code(request, code):
    project = models.Project.objects.get(code=code)
    return render(request, 'tasks/project.html',
                  {'project': project})
