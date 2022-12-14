from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tasks/', views.tasksToDo, name="tasks"),
    path('add/', views.add, name="add"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('edit/<str:pk>/', views.editTask, name="edit"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]