from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView
from .views import journals, trades, jform, tform, updateJournal

urlpatterns = [
    path('', LoginView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('journals/', journals, name='journals'),
    path('trades/<int:journal_id>/', trades, name='trades'),
    path('jform/', jform, name='jform'),
    path('tform/<int:journal_id>/', tform, name='tform'),
    path('update-journal/<int:journal_id>/', updateJournal, name='update-journal'),
]
