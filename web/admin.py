from django.contrib import admin
from .models import Income, Expense
from jalali_date.admin import ModelAdminJalaliMixin
from jalali_date import datetime2jalali

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'created', 'updated', 'user')
    list_filter = ("title", "amount")
    search_fields = ('title', 'amount', 'created', 'updated', 'user')
    prepopulated_fields = {'slug' : ('title',)}
    def get_created_jalali(self, obj):
	    return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'created', 'updated', 'user')
    list_filter = ("title", "amount")
    search_fields = ('title', 'amount', 'created', 'updated', 'user')
    prepopulated_fields = {'slug' : ('title',)}

    def get_created_jalali(self, obj):
	    return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')