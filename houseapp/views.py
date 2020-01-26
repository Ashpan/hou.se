from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, RedirectView

from .models import Task
from .forms import JoinForm
from .models import Task, House, Membership
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, RedirectView
from django.views.generic.edit import FormMixin
from datetime import date


<<<<<<< Updated upstream
def home(request):
    context = {
        'tasks': Task.objects.all(),
    }

    return render(request, 'houseapp/home.html', context)


=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    context = {
        'tasks': Task.objects.all()
    }
=======
    if not request.user.is_authenticated:
        return render(request, 'houseapp/splash.html')
    try:
        user_house = Membership.objects.get(person=request.user).house

        context = {
            'tasks': Task.objects.filter(user__in=user_house.members.all())
        }
>>>>>>> Stashed changes

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
        return super().form_valid(form)


def createhouse(request):
    return render(request, 'registration/CreateHouse.html')


def joinhouse(request):
    return render(request, 'registration/JoinHouse.html')

<<<<<<< Updated upstream
def createorjoin(request):
    return render(request, 'registration/createorjoin.html')

=======
>>>>>>> Stashed changes

def splash(request):
    if request.user.is_authenticated:
        return render(request, 'houseapp/home.html')

    return render(request, 'houseapp/splash.html')


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


class JoinHouseView(CreateView):
    model = Membership
    fields = ['house']
    success_url = '/'



    def post(self, request):
        inv = request.POST['invite-code-input']
        house = House.objects.get(invite_code=inv)
        mem = Membership(person=request.user, house=house,
                         date_joined=date.today())
        mem.save()

        return HttpResponseRedirect('/')


# def form_valid(self, form):
#     if form.request == 'POST':
#         print(form.request.POST)
#     return super().form_valid(form)
