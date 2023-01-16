from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView
from .views import deleteJournal, trades, jform, tform, updateJournal, updateTrade

urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('journals/', deleteJournal, name='journals'),
    path('trades/<int:journal_id>/', trades, name='trades'),
    path('jform/', jform, name='jform'),
    path('tform/<int:journal_id>/', tform, name='tform'),
    path('update-journal/<int:journal_id>/', updateJournal, name='update-journal'),
    path('update-trade/<int:journal_id>/<int:trade_id>/', updateTrade, name='update-trade'),
]
