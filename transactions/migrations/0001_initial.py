# Generated by Django 4.2.7 on 2023-11-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')], max_length=10)),
                ('client_name', models.CharField(max_length=255)),
                ('client_id_passport', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyTransferTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=255)),
                ('sender_id_passport', models.CharField(max_length=255)),
                ('transaction_type', models.CharField(choices=[('send', 'Send Money'), ('receive', 'Receive Money')], max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('company', models.CharField(choices=[('western_union', 'Western Union'), ('moneygram', 'MoneyGram'), ('mpesa', 'M-Pesa')], max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]