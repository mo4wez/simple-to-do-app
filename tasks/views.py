from django.shortcuts import render
from django.http import HttpResponse

def task_list_view(request):
    return render(request, 'tasks/task_list.html')