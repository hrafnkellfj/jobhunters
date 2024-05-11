from django.forms import ModelForm, widgets
from job.models import Experience


class StepFourCreateForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['applicant', 'applied_job']
        widgets = {
            'company': widgets.TextInput(attrs={'class': 'form-control'}),
            'experience_role': widgets.TextInput(attrs={'class': 'form-control'}),
            'experience_start': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'experience_end': widgets.TextInput(attrs={'class': 'form-control datepicker'})
        }

