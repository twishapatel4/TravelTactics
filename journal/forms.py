from django import forms
from .models import TravelJournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = TravelJournalEntry
        fields = ['image', 'caption']