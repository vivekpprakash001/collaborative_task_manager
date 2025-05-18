from rest_framework import serializers
from .models import Task, TaskUpdate


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'assigned_users', 'status']


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUpdate
        fields = ['id', 'task', 'updated_by', 'timestamp', 'update_text']
