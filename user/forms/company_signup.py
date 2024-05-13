from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from user.models import companyProfile
from company.models import Company
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form


class CustomUserCreationForm2(UserCreationForm):

    title = forms.CharField(label='Nafn Fyrirtækis', max_length=50)
    email = forms.EmailField(label='Tölvupóstfang')
    username = forms.CharField(label='Notendanafn', min_length=5, max_length=150)
    password1 = forms.CharField(label='Lykilorð', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Staðfesta lykilorð', widget=forms.PasswordInput)

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if Company.objects.filter(title=title).exists():
            raise ValidationError("Fyrirtæki með þetta nafn nú þegar til")
        return title

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()
        if User.objects.filter(email=email).exists():
            raise ValidationError("Netfang til nú þegar")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').lower()
        if User.objects.filter(username=username).exists():
            raise ValidationError("Notandi til með þetta notendanafn")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Lykilorð eru ekki eins")
        return password2

    def save(self, commit=True):
        with transaction.atomic():
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
                password=self.cleaned_data['password1']
            )
            company = Company.objects.create(
                title=self.cleaned_data['title'].capitalize()
            )
            return user, company
