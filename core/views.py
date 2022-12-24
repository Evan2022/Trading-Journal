from django.shortcuts import render
from .forms import CustomLoginForm


def login_view(request):
    form = CustomLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)
