from django.urls import path
from .views import TaskListView, TaskCreateView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('house/', views.house, name='house'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
]
