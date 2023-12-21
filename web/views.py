from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeCreateForm, ExpenseCreateForm, IncomeUpdateForm, ExpenseUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from jalali_date import datetime2jalali, date2jalali

def calender(request):
    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')

def home(request):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()
    return render(request, "web/index.html", {"expenses" : expenses, "incomes" : incomes})

@login_required(login_url="accounts:user_login")
def income_detail(request, income_id):
    incomes = Income.objects.filter(id=income_id)
    return render(request, "web/income_detail.html", {"incomes" : incomes})

@login_required(login_url="accounts:user_login")
def expense_detail(request, expense_id):
    expenses = Expense.objects.filter(id=expense_id)
    return render(request, "web/expense_detail.html", {"expenses" : expenses})

@login_required(login_url="accounts:user_login")
def income_delete(request, income_id):
    income = Income.objects.filter(id=income_id).delete()
    messages.success(request, "درآمد با موفقیت حذف شد", 'success')
    return redirect("web:home")

@login_required(login_url="accounts:user_login")
def expense_delete(request, expense_id):
    expense = Expense.objects.filter(id=expense_id).delete()
    messages.success(request, "خرج با موفقیت حذف شد", 'success')
    return redirect("web:home")

@login_required(login_url="accounts:user_login")
def income_create(request):
    if request.method == "POST":
        form = IncomeCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Income.objects.create(user=request.user, title=cd["title"], amount=cd["amount"])
            messages.success(request, "درآمد با موفقیت ساخته شد", 'success')
            return redirect("web:home")
    else:
        form = IncomeCreateForm()
    return render(request, "web/income_create.html", {"form" : form})

@login_required(login_url="accounts:user_login")
def expense_create(request):
    if request.method == "POST":
        form = ExpenseCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Expense.objects.create(user=request.user, title=cd["title"], amount=cd["amount"])
            messages.success(request, "خرج با موفقیت ساخته شد", 'success')
            return redirect("web:home")
    else:
        form = ExpenseCreateForm()
    return render(request, "web/expense_create.html", {"form" : form})

@login_required(login_url="accounts:user_login")
def income_update(request, income_id):
    income = Income.objects.get(id=income_id)
    if request.method == "POST":
        form = IncomeUpdateForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, "درآمد با موفقیت تغییر یافت", 'success')
            return redirect("web:income_detail", income_id)
    else:
        form = IncomeUpdateForm(instance=income)
    return render(request, "web/income_edit.html", {"form" : form})

@login_required(login_url="accounts:user_login")
def expense_update(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.method == "POST":
        form = ExpenseUpdateForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "خرج با موفقیت تغییر یافت", 'success')
            return redirect("web:expense_detail", expense_id)
    else:
        form = ExpenseUpdateForm(instance=expense)
    return render(request, "web/expense_edit.html", {"form" : form})

def error_404(request, Exeption):
    return render(request, "404.html")