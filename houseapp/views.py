from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, RedirectView
from django.views.generic.edit import FormMixin

from .models import Task, House


def home(request):
    context = {
        'tasks': Task.objects.all(),
    }

    return render(request, 'houseapp/home.html', context)


def house(request):
    return render(request, 'houseapp/house.html')


def tasks(request):
    content = {
        'tasks': Task.objects.all()
    }
    return render(request, 'houseapp/tasks.html', content)


def calendar(request):
    return render(request, 'houseapp/calendar.html')


class TaskListView(ListView):
    model = Task
    template_name = 'houseapp/home.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'due_date', 'user']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class TaskCompleteView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.completed = True
        task.save(update_fields=['completed'])
        print("Completed", task)
        return super().get_redirect_url(*args)


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"


class CreateHouseView(CreateView):
    model = House
    fields = ['name', 'address', 'invite_code']
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)
