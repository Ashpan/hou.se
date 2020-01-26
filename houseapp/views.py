from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from .models import Task, House, Membership
from .forms import HouseRegisterForm


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


class CreateHouseView(CreateView):
    model = House
    fields = ['name', 'address']
    success_url = '/'

    def form_valid(self, form):
        print(type(self.request.user))
        form.instance.save()
        form.instance.members.add(self.request.user)
        return super().form_valid(form)


class JoinHouseView(CreateView):
    model = Membership
    fields = ['house']
    success_url = '/'

    def form_valid(self, form):
        form.instance.person = self.request.user
        return super().form_valid(form)

# def createhouse(request):
#     if request.method == 'POST':
#         new_form = HouseRegisterForm(request.POST, instance=request.user)
#         if new_form.is_valid():
#             new_form.save()
#     else:
#         new_form = HouseRegisterForm(instance=request.user)
#     context = {
#         'new_form': new_form
#     }
#     return render(request, 'registration/CreateHouse.html', context)


def joinhouse(request):

    return render(request, 'registration/JoinHouse.html')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = "/"
