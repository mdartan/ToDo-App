import imp
from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm

from .models import todo

class TodoForm(ModelForm):
    class Meta:
        model = todo
        fields = ('ToDo', 'Status')
        labels = {
            'ToDo': 'Action To Do',
            'Status': 'Select Status',
        }
        widgets = {
            'ToDo': forms.TextInput(attrs={'class': 'form-control'}),
            'Status': forms.Select(attrs={'class': 'form-select', 'multiple aria-label': 'multiple select example'}),
        }