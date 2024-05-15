from django.forms import ModelForm, widgets
from company.models import Company


class ChangeCompanyProfile(ModelForm):
    class Meta:
        model = Company
        exclude = ['address']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'logo': widgets.TextInput(attrs={'class': 'form-control'}),
            'coverImage': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'class': 'form-control'})
        }