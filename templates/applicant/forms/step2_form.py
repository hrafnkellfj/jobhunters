from django.forms import ModelForm, widgets
from applicant.models import Applicant


class StepTwoCreateForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['photo', 'username', 'email', 'name', 'street', 'houseNr', 'city', 'postalCode', 'country', 'phone']
        widgets = {
            'aboutMe': widgets.Textarea(attrs={'class': 'form-control'})
        }
