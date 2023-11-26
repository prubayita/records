from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(BankTransaction)
class BankTransactionAdmin(admin.ModelAdmin):
    list_display = ['bank_name','transaction_type','client_name', 'amount', 'date']


@admin.register(MoneyTransferTransaction)
class MoneyTransferTransactionAdmin(admin.ModelAdmin):
    list_display = ['company','sender_name','transaction_type', 'location', 'date']
