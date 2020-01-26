from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('house/', views.house, name='house-settings'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('house/create/', views.createhouse, name='house-create'),
    path('house/join/', views.joinhouse,name="house-join"),
    path('splash/', views.splash,name="splash"),
]
