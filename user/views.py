from django.shortcuts import render, redirect
from templates.user.forms.signup_form import CustomUserCreationForm


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
    return render(request, 'user/profile.html')