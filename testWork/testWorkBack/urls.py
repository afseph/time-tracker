from django.urls import path, include

from .views import task_list, add_task

urlpatterns = [
    path('', task_list, name="index"),
    path("add_task/", add_task, name="add_task"),
]