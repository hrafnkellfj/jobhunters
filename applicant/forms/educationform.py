from django.forms import ModelForm, widgets
from applicant.models import Education


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['applicant']
        widgets = {
            'school': widgets.TextInput(attrs={'class': 'form-control'}),
            'degree': widgets.TextInput(attrs={'class': 'form-control'}),
            'fieldOfStudy': widgets.TextInput(attrs={'class': 'form-control'}),
            'start': widgets.TextInput(attrs={'class': 'form-control datepicker'}),
            'end': widgets.TextInput(attrs={'class': 'form-control datepicker'})
        }
        labels= {
            'school': 'Skóli',
            'degree': 'Gráða',
            'fieldOfStudy': 'Námssvið',
            'start': 'Upphaf náms',
            'end': 'Lok náms'
        }