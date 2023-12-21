from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path('', views.home, name="home"),
    path('income/detail/<int:income_id>', views.income_detail, name="income_detail"),
    path('expense/detail/<int:expense_id>', views.expense_detail, name="expense_detail"),
    path('income/delete/<int:income_id>', views.income_delete, name="income_delete"),
    path('expense/delete/<int:expense_id>', views.expense_delete, name="expense_delete"),
    path('income/create', views.income_create, name="income_create"),
    path('expense/create', views.expense_create, name="expense_create"),
    path('income/edit/<int:income_id>', views.income_update, name="income_update"),
    path('expense/edit/<int:income_id>', views.expense_update, name="expense_update"),
]