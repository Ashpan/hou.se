from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskCompleteView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('house/', views.house, name='house'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:pk>/complete/', TaskCompleteView.as_view(), name='task-complete'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete")
]
