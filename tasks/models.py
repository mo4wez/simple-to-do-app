from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)

    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.pk})
    