from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
]