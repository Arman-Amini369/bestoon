from django import forms
from .models import Income, Expense

class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ()