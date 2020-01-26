from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, CreateHouseView, JoinHouseView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('house/settings', views.house, name='house-settings'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('createhouse/', CreateHouseView.as_view(), name='house-create'),
    path('house/join/', JoinHouseView.as_view(), name='house-join')
]
