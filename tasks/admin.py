from django.contrib import admin

from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'title',
        'is_complete',
        'datetime_created',
    ]

    ordering = ['is_complete']