from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('house/', views.house, name='house'),
    path('tasks/', views.tasks, name='tasks'),
    path('calendar/', views.calendar, name='calendar'),
]
