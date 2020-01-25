from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Task


def home(request):
    context = {
        'tasks': Task.objects.all()
    }

    return render(request, 'houseapp/home.html')


def house(request):
    return render(request, 'houseapp/house.html')


def tasks(request):
    return render(request, 'houseapp/tasks.html')


def calendar(request):
    return render(request, 'houseapp/calendar.html')


class TaskListView(ListView):
    model = Task
    template_name = 'houseapp/home.html'
    context_object_name = 'tasks'