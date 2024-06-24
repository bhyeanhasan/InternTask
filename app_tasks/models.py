from django.db import models

from app_projects.models import Project
from app_users.models import User


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default='todo',
                              choices=[('todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')])
    priority = models.CharField(max_length=50, default='low',
                                choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
