# Generated by Django 4.2.7 on 2024-02-06 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_moneytransfertransaction_amount_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='banktransaction',
            unique_together={('client_id_passport', 'amount', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='moneytransfertransaction',
            unique_together={('sender_id_passport', 'amount', 'date')},
        ),
    ]
