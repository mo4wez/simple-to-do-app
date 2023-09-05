from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list_view, name='tasks_list'),
]
