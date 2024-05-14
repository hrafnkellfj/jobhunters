from django.forms import ModelForm, widgets
from applicant.models import Applicant


class ApplicantFormAll(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNr': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postalCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'aboutMe': widgets.Textarea(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Nafn',
            'street': 'Götuheiti',
            'houseNr': 'Húsnúmer',
            'city': 'Bæjarfélag',
            'postalCode': 'Póstnúmer',
            'country': 'Land',
            'phone': 'Símanúmer',
            'aboutMe': 'Um mig',
            'photo': 'Prófílmynd',
            'email': 'Netfang'
        }

class ApplicantFormPrimary(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id', 'phone', 'aboutMe', 'photo', 'email']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'houseNr': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
            'postalCode': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            #'email': widgets.EmailInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nafn',
            'street': 'Götuheiti',
            'houseNr': 'Húsnúmer',
            'city': 'Bæjarfélag',
            'postalCode': 'Póstnúmer',
            'country': 'Land',

        }

class ApplicantFormSecondary(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['id', 'name', 'street', 'houseNr', 'city', 'postalCode', 'country']
        widgets = {
            'phone': widgets.NumberInput(attrs={'class': 'form-control'}),
            'aboutMe': widgets.Textarea(attrs={'class': 'form-control'}),
            'photo': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'})
        }
        labels = {
            'phone': 'Símanúmer',
            'aboutMe': 'Um mig',
            'photo': 'Prófílmynd',
            'email': 'Netfang'
        }