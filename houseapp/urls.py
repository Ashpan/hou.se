from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView
from . import views

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('house/', views.house, name='house'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/new/', TaskCreateView.as_view(), name='task-create'),
    path('calendar/', views.calendar, name='calendar'),
<<<<<<< Updated upstream
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete")
=======
    path('tasks/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('createhouse/', views.createhouse, name='house-create'),
>>>>>>> Stashed changes
]
