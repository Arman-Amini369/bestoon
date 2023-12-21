from django import forms
from .models import Income, Expense

class IncomeCreateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('title', 'amount')
        labels = {
            "title" : ("موضوع"),
            "amount" : ("مقدار"),
        }

class ExpenseCreateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'amount')
        labels = {
            "title" : ("موضوع"),
            "amount" : ("مقدار"),
        }
    
class IncomeUpdateForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('title', 'amount')
        labels = {
            "title" : ("موضوع"),
            "amount" : ("مقدار"),
        }

class ExpenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'amount')
        labels = {
            "title" : ("موضوع"),
            "amount" : ("مقدار"),
        }