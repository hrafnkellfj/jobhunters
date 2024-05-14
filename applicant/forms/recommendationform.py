from django.forms import ModelForm, widgets
from job.models import Recommendation


class RecommendationForm(ModelForm):
    class Meta:
        model = Recommendation
        exclude = ['applicant', 'job']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'class': 'form-control'}),
            'allowedToContact': widgets.CheckboxInput()
        }

        labels = {
            'name': 'Nafn meðmælenda',
            'email': 'Tölvpóstfang',
            'phone': 'Sími',
            'role': 'Staða',
            'allowedToContact': 'Má hafa samband'
        }