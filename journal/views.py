from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import CustomLoginForm, CustomSignupForm
from journal.models import Journal, Trade


def login_view(request):
    form = CustomLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def signup_view(request):
    form = CustomSignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)
