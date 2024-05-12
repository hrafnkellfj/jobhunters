from django.forms import ModelForm, widgets
from applicant.models import ApplicantEducation


class EducationForm(ModelForm):
    class Meta:
        model = ApplicantEducation
        exclude = ['applicant']
        widgets = {
            'school': widgets.TextInput(attrs={'class': 'form-control'}),
            'degree': widgets.TextInput(attrs={'class': 'form-control'}),
            'fieldOfStudy': widgets.TextInput(attrs={'class': 'form-control'}),
            'education_start': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'education_end': widgets.TextInput(attrs={'class': 'form-control datepicker'})
        }
