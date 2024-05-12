from django.forms import ModelForm, widgets
from applicant.models import Applicant


class StepOneCreateForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['photo', 'email', 'aboutMe', 'phone']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNr': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postalCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'})
        }
