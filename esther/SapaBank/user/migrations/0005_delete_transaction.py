# Generated by Django 5.1.3 on 2024-11-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_account_account_no_alter_account_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
