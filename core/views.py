from django.shortcuts import render
from .forms import CustomLoginForm, CustomSignupForm


def login_view(request):
    form = CustomLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def signup_view(request):
    form = CustomSignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)
