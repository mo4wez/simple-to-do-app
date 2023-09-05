from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = 'tasks/task_create.html'
    fields = '__all__'

class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'tasks/task_update.html'
    fields = '__all__'

class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks_list')