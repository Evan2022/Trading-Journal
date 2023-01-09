from django.shortcuts import render, redirect
from core.forms import CustomLoginForm, CustomSignupForm
from journal.models import Journal, Trade


def login_view(request):
    form = CustomLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def signup_view(request):
    form = CustomSignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


def journals(request):
    return render(request, 'journals.html',)


def trades(request):
    return render(request, 'trades.html',)
