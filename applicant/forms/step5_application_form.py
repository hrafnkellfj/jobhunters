from django.forms import ModelForm, widgets
from job.models import Recommendation


class StepFiveCreateForm(ModelForm):
    class Meta:
        model = Recommendation
        exclude = ['applicant', 'job']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'class': 'form-control'}),
            'allow_contact': widgets.CheckboxInput(attrs={'class': 'form-control'})
        }
