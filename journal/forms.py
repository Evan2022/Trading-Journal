from django.forms import ModelForm
from . models import Journal, Trade


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
