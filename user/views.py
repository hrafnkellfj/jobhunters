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
        if request.method == "POST":
            print(1)
        return render(request, 'user/applicant_profile.html', {
            "form": ""
        })
    c_user = companyProfile.objects.filter(user=request.user).first()
    if request.method == "POST":
        print(2)
    return render(request, 'user/user_profile.html', {
        "form":""
    })
