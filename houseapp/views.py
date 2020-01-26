from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from .models import Task


def house(request):
    return render(request, 'houseapp/house_settings.html')


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
        form.instance.author = self.request.user
        return super().form_valid(form)

def createhouse(request):
    return render(request, 'registration/CreateHouse.html')

def joinhouse(request):
    return render(request, 'registration/JoinHouse.html')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"
