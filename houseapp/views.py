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

def home(request):
    context = {
        'tasks': Task.objects.all()
    }

    if request.user.is_authenticated:
        return render(request, 'houseapp/home.html', context)
    else:
        return render(request, 'houseapp/splash.html')

class TaskListView(ListView):
    model = Task
    template_name = 'houseapp/home.html'
    context_object_name = 'tasks'

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('splash')



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

def splash(request):
    if request.user.is_authenticated:
        return render(request, 'houseapp/home.html')

    return render(request, 'houseapp/splash.html')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"
