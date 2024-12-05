from django.db import models
from django.contrib.auth.models import User

import time
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=10, unique=True)
    account_balance = models.IntegerField(default=0)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user}: ₦{self.account_balance}"

class Transaction_history(models.Model):
    primary_account = models.OneToOneField(Account, on_delete = models.CASCADE)



class Transaction(models.Model):
    transaction_history = models.ForeignKey(Transaction_history, related_name="transactions", on_delete =models.CASCADE) 
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    sender = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="sender")
    receiver = models.ForeignKey(Account, on_delete=models.DO_NOTHING, related_name="receiver")

class Withdrawal(models.Model):
    pass 
