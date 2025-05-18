from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('freezed', 'Freezed'),
        ('pending', 'Pending')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_users = models.ManyToManyField(User, related_name='assigned_tasks')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return self.title


class TaskUsers(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='tasks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_user')

    def __str__(self):
        return self.task


class TaskUpdate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='updates')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    update_text = models.TextField()

    def __str__(self):
        return f"Update for {self.task.title} by {self.updated_by}"
