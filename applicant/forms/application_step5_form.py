from django.forms import ModelForm, widgets
from job.models import Recommendation


class StepFiveCreateForm(ModelForm):
    class Meta:
        model = Recommendation
        exclude = ['applicant', 'applied_job']
        widgets = {
            'recommendation_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'recommendation_email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'recommendation_phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'recommendation_role': widgets.TextInput(attrs={'class': 'form-control'}),
            'allow_contact': widgets.CheckboxInput(attrs={'class': 'form-control'})
        }
