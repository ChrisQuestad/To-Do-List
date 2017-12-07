from django import forms
from django.forms.models import ModelForm
from .models import List, Task

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['title', 'description']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'due_date']
