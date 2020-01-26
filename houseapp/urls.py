from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskCompleteView, CreateHouseView, JoinHouseView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('house/', views.house, name='house-settings'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:pk>/complete/',
         TaskCompleteView.as_view(), name='task-complete'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('house/create/', views.createhouse, name='house-create'),
    path('house/join/', views.joinhouse,name="house-join"),
    path('splash/', views.splash,name="splash"),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete"),
    path('house/create/', CreateHouseView.as_view(), name='house-create'),
    path('house/join/', JoinHouseView.as_view(), name='house-join'),
    path('createorjoin/', views.createorjoin,name='create-or-join'),
]
