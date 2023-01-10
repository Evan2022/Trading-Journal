from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

@login_required
def journals(request):
    return render(request, 'journals.html',)

@login_required
def trades(request):
    return render(request, 'trades.html',)
