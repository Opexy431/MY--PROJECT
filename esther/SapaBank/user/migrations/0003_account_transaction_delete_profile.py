# Generated by Django 5.1.3 on 2024-11-28 16:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_account_profile_account_no_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=10)),
                ('account_balance', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=18)),
                ('phone', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='receiver', to='user.account')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sender', to='user.account')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
