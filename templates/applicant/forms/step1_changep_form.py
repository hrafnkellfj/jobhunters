from django.forms import ModelForm, widgets
from applicant.models import Applicant


class StepOneChangeProfile(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['username', 'postalCode', 'city', 'country']
        widgets = {
            'photo': widgets.FileInput(attrs={'class': 'form-control'}),
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNr': widgets.TextInput(attrs={'class': 'form-control'}),
            'aboutMe': widgets.Textarea(attrs={'class': 'form-control'}),
        }
