from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path('', views.home, name="home"),
    path('income/detail/<str:slug>', views.income_detail, name="income_detail"),
    path('expense/detail/<str:slug>', views.expense_detail, name="expense_detail"),
    path('income/delete/<str:slug>', views.income_delete, name="income_delete"),
    path('expense/delete/<str:slug>', views.expense_delete, name="expense_delete"),
]