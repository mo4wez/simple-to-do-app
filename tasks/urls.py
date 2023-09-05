from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list_view, name='tasks_list'),
    path('tasks/<int:pk>/', views.task_detail_view, name='task_detail')
]
