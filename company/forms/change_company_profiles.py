from django.forms import ModelForm, widgets
from company.models import Company


class ChangeCompanyProfile(ModelForm):
    class Meta:
        model = Company
        exclude = ['id']
        widgets = {
            'title': widgets.TextInput(attrs={'class': 'form-control'}),
            'logo': widgets.TextInput(attrs={'class': 'form-control'}),
            'coverImage': widgets.TextInput(attrs={'class': 'form-control'}),
            'address': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Titill',
            'logo': 'Merki',
            'coverImage': 'Mynd fyrir bakgrunn',
            'description': 'Lýsing',
            'address': 'Heimilisfang'
        }