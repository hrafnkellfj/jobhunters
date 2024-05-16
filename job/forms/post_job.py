from django.forms import ModelForm, widgets,ChoiceField, Select
from django import forms
from job.models import Job


class PostJob(ModelForm):

    JOB_PERCENTAGE_CHOICES = [
        ('Hlutastarf', 'Hlutastarf'),
        ('Fullt starf', 'Fullt starf')]

    jobPercentage = forms.MultipleChoiceField(
        choices=JOB_PERCENTAGE_CHOICES,
        widget=forms.CheckboxSelectMultiple(),
        label='Starfshlutfall'
    )

    class Meta:
        model = Job
        exclude = ['id', 'company', 'postDate']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'dueDate': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'startDate': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'jobImage': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'})
        }
        labels={
            'title': 'Titill',
            'description': 'Lýsing',
            'location': 'Staðsetning',
            'dueDate': 'Umsóknarfrestur',
            'startDate': 'Hefja störf',
            'jobImage': 'Mynd',
            'category': 'Starfssvið',
        }