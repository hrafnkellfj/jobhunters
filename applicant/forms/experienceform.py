from django.forms import ModelForm, widgets
from job.models import Experience


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['applicant', 'job']
        widgets = {
            'company': widgets.TextInput(attrs={'class': 'form-control'}),
            'role': widgets.TextInput(attrs={'class': 'form-control'}),
            'start': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'end': widgets.TextInput(attrs={'class': 'form-control datepicker'})
        }

        labels = {
            'company': 'Fyrirtæki',
            'role': 'Staða',
            'start': 'Upphaf starfs',
            'end': 'Lok starfs'
        }