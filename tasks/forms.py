from django import forms
from .models import Task

from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.models import User  # or get_user_model if custom user
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_description', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-select', 'id': 'id_status'}),
        }

