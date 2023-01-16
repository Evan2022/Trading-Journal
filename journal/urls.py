from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView
from .views import journals, trades, forms


urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('journals/', journals, name='journals'),
    path('trades/<int:journal_id>/', trades, name='trades'),
    path('forms/', forms, name='forms'),
]