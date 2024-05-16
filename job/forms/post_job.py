from django.forms import ModelForm, widgets,ChoiceField, Select
from django import forms
from job.models import Job


class PostJob(ModelForm):

    JOB_PERCENTAGE_CHOICES = [
        ('Hlutastarf', 'Hlutastarf'),
        ('Fullt starf', 'Fullt starf'),
        ('Fullt starf / Hlutastarf', "Fullt starf / Hlutastarf")]

    jobPercentage = forms.MultipleChoiceField(
        choices=JOB_PERCENTAGE_CHOICES,
<<<<<<< HEAD
        widget=forms.ChoiceField()
=======
        widget=forms.CheckboxSelectMultiple(),
        label='Starfshlutfall'
>>>>>>> main
    )

    class Meta:
        model = Job
        exclude = ['id', 'company', 'postDate', 'location']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'}),
            'location': widgets.TextInput(attrs={'class': 'form-control'}),
            'dueDate': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'startDate': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
<<<<<<< HEAD
            'jobImage': widgets.TextInput(attrs={'class': 'form-control'}),
            'category': widgets.Select(attrs={'class': 'form-control'}),
            'jobPercentage': widgets.Select(attrs={'class': 'form-control'})
=======
            'category': widgets.Select(attrs={'class': 'form-control'})
>>>>>>> main
        }
        labels={
            'title': 'Titill',
            'description': 'Lýsing',
            'dueDate': 'Umsóknarfrestur',
            'startDate': 'Hefja störf',
            'category': 'Starfssvið',
        }