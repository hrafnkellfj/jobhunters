from django.forms import ModelForm, widgets,ChoiceField, Select
from django import forms
from job.models import Job


class PostJob(ModelForm):

    JOB_PERCENTAGE_CHOICES = [(i, f"{i}%") for i in range(10, 101, 10)]  # Generating choices from 10% to 100%

    jobPercentage = forms.ChoiceField(
        choices=JOB_PERCENTAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Job
        exclude = ['id', 'company', 'postDate']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'dueDate': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'startDate': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'jobImage': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'})
        }