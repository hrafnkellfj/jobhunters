from django.shortcuts import render, redirect
from templates.user.forms.signup_form import CustomUserCreationForm
from user.models import applicantProfile, companyProfile


def login(request):
    return render(request, 'user/login.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    return render(request, 'user/signup.html', {
        'form': CustomUserCreationForm()
    })


def profile(request):
    a_user = applicantProfile.objects.filter(user=request.user).first()
    if a_user:
        applicant = a_user.applicant
        if request.method == "POST":
            print(1)
        return render(request, 'user/applicant_profile.html', {
            "form": "", "applicant": applicant
        })
    c_user = companyProfile.objects.filter(user=request.user).first()
    if c_user:
        company = c_user.company
        if request.method == "POST":
            print(2)
        return render(request, 'user/user_profile.html', {
            "form":"", "company": company
        })
    #return server error, því ef hægt er að búa til notanda sem ekki er tengdur við applicant og company þá er það okkur að kenna
