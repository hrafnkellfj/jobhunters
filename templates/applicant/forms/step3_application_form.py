from django.forms import ModelForm, widgets
from applicant.models import ApplicantEduction


class StepThreeCreateForm(ModelForm):
    class Meta:
        model = ApplicantEduction
        exclude = ['applicant']
        widgets = {
            'school': widgets.TextInput(attrs={'class': 'form-control'}),
            'degree': widgets.TextInput(attrs={'class': 'form-control'}),
            'field_of_study': widgets.TextInput(attrs={'class': 'form-control'}),
            'start': widgets.DateInput(attrs={'class': 'form-control'}),
            'end': widgets.DateInput(attrs={'class': 'form-control'})
        }
