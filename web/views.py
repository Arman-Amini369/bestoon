from django.shortcuts import render, redirect
from .models import Income, Expense
from django.contrib import messages
from jalali_date import datetime2jalali, date2jalali

def calender(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


def home(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()
    return render(request, "web/index.html", {"expenses" : expenses, "incomes" : incomes})

def income_detail(request, slug):
    incomes = Income.objects.filter(slug=slug)
    return render(request, "web/income_detail.html", {"incomes" : incomes})

def expense_detail(request, slug):
    expenses = Expense.objects.filter(slug=slug)
    return render(request, "web/expense_detail.html", {"expenses" : expenses})

def income_delete(request, slug):
    income = Income.objects.filter(slug=slug).delete()
    messages.success(request, "درآمد با موفقیت حذف شد", 'success')
    return redirect("web:home")

def expense_delete(request, slug):
    expense = Expense.objects.filter(slug=slug).delete()
    messages.success(request, "خرج با موفقیت حذف شد", 'success')
    return redirect("web:home")

def income_create(request):
    pass