from django.db import models

# Create your models here.
# models.py

class BankTransaction(models.Model):
    BANK_CHOICES = [
        ('equity_bank', 'Equity Bank'),
        ('bk', 'BK'),
        ('ecobank', 'Ecobank'),
    ]
    bank_name = models.CharField(max_length=255, choices=BANK_CHOICES)
    transaction_type = models.CharField(max_length=10, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')])
    client_name = models.CharField(max_length=255)
    client_id_passport = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

class MoneyTransferTransaction(models.Model):
    COMPANY_CHOICES = [
        ('western_union', 'Western Union'),
        ('moneygram', 'MoneyGram'),
        ('mpesa', 'M-Pesa'),
        ('dubai', 'Dubai'),
    ]

    sender_name = models.CharField(max_length=255)
    sender_id_passport = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=10, choices=[('send', 'Send Money'), ('receive', 'Receive Money')])
    location = models.CharField(max_length=255)
    company = models.CharField(max_length=20, choices=COMPANY_CHOICES)
    date = models.DateField(auto_now_add=True)