from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView
from .views import journals, trades


urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('journals/', journals, name='journals'),
]