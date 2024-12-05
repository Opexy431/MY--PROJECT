from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *

import random

def generate_account_number(length=10):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    return ''.join(random.choices(numbers, k=length))

def home(request):
    user = request.user
    if user.is_authenticated:
        context = {
            "shit":user,
            "balance":user.account.account_balance
        }
    else:
        context = {}
    return render(request, "home.html", context)

def login_page(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        age = request.POST.get('age')
        # if age < 18:
        #     childaccount = 
        if form.is_valid():
            user = form.save(commit=False)
            user_profile = Account(user=user, account_no=generate_account_number())
            user.save()
            user_profile.save()
            return redirect('login')
    context = {
        "form":form
    }
    return render(request, 'register.html', context)
from django.shortcuts import render, redirect
from .models import Transaction

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def create_transaction(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        transaction = Transaction(amount=amount, status='pending')
        transaction.save()
        return redirect('transaction_list')
    return render(request, 'transactions/create_transaction.html')
