from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView

from .models import Task

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

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'due_date', 'user']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

