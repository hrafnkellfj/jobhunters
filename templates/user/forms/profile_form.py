from django.forms import ModelForm, widgets
from applicant.models import Applicant, ApplicantEduction


class Profile(ModelForm):
    class Meta:
        model = Applicant, ApplicantEduction
        exclude = ['email', 'phone', 'street', 'houseNr', 'city', 'country', 'postalCode']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'aboutMe': widgets.Textarea(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'school': widgets.TextInput(attrs={'class': 'form-control'}),
            'degree': widgets.TextInput(attrs={'class': 'form-control'}),
            'fieldOfStudy': widgets.TextInput(attrs={'class': 'form-control'}),
            'start': widgets.DateInput(attrs={'class': 'form-control'}),
            'end': widgets.DateInput(attrs={'class': 'form-control'})
        }

