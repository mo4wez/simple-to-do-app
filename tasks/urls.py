from django.urls import path

from .views import TaskListView, TaskDetailView

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]
