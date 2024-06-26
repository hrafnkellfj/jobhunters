from django.forms import ModelForm, widgets
from job.models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ['status', 'applyDate', 'resultDate', 'applicant', 'job', 'isFinished']
        widgets = {
            'coverLetter': widgets.Textarea(attrs={'class': 'form-control'})
        }
        labels={
            'coverLetter': 'Kynningarbréf'

        }
