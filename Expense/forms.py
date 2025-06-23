from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date']  # Fields to fill in the form
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Date input field
        }