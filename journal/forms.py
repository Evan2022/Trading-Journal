from django.forms import ModelForm
from . models import Journal, Trade
from django import forms
from django.forms.widgets import DateTimeInput

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['currency', 'name', 'starting_balance']

    def save(self, user, commit=True):
        journal = super().save(commit=False)
        journal.user = user
        if commit:
            journal.save()
        return journal


class TradeForm(ModelForm):
    datetime = forms.DateTimeField(
        widget=DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M',
        ),
        input_formats=['%Y-%m-%dT%H:%M'],
    )

    class Meta:
        model = Trade
        exclude = ['journal']
