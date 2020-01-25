from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'houseapp/home.html')


def house(request):
    return render(request, 'houseapp/house.html')


def tasks(request):
    return render(request, 'houseapp/tasks.html')


def calendar(request):
    return render(request, 'houseapp/calendar.html')
