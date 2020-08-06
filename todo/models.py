from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(
        help_text="Enter todo list separated by comma:"
    )

    def __str__(self):
        return self.title

    def get_text(self):
        return [i.strip() for i in self.text.split(",")]

