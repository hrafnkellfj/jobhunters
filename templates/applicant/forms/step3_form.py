from django.forms import ModelForm, widgets
from job.models import Experience


class StepThreeCreateForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['applicant', 'applied_job']
        widgets = {
            'company': widgets.TextInput(attrs={'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'class': 'form-control'}),
            'start': widgets.DateInput(attrs={'class': 'form-control'}),
            'end': widgets.DateInput(attrs={'class': 'form-control'}),
        }  
