from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .models import *
# Create your views here.

def login(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('overview')  # Redirect to the desired page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'cre/login.html')


def logout_view(request):
    logout(request)
    return redirect('login') 

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        # role = request.POST['role']  # Get the selected role from the dropdown

        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        # Redirect to the desired page after successful signup (e.g., login page)
        return redirect('login')
       
    return render(request, 'cre/signup.html')


# def overview(request):
#   template = loader.get_template('ui/test2.html')
#   return HttpResponse(template.render())

def overview(request):
    # Get filter parameters from GET request
    bank_name = request.GET.get('bank_name')
    transaction_type = request.GET.get('transaction_type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Get all transactions by default
    transactions = BankTransaction.objects.all()

    # Apply filters based on parameters
    if bank_name:
        transactions = transactions.filter(bank_name=bank_name)
    if transaction_type:
        transactions = transactions.filter(transaction_type=transaction_type)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    template = 'ui/test2.html'
    context = {'transactions': transactions}
    return render(request, template, context)

def bank_record(request):
    if request.method == 'POST':
        # Retrieve data from the form
        bank_name = request.POST.get('bank_name')
        transaction_type = request.POST.get('transaction_type')
        client_name = request.POST.get('client_name')
        client_id_passport = request.POST.get('client_id_passport')
        amount = request.POST.get('amount')

        # Create a new BankTransaction instance and save it
        BankTransaction.objects.create(
            bank_name=bank_name,
            transaction_type=transaction_type,
            client_name=client_name,
            client_id_passport=client_id_passport,
            amount=amount
        )

        return redirect('overview')  # Redirect to the overview page or any other page

    template = 'ui/rec.html'
    return render(request, template)

def mt_record(request):
    if request.method == 'POST':
        # Retrieve data from the form
        sender_name = request.POST.get('sender_name')
        sender_id_passport = request.POST.get('sender_id_passport')
        transaction_type = request.POST.get('transaction_type')
        location = request.POST.get('location')
        company = request.POST.get('company')

        # Create a new MoneyTransferTransaction instance and save it
        MoneyTransferTransaction.objects.create(
            sender_name=sender_name,
            sender_id_passport=sender_id_passport,
            transaction_type=transaction_type,
            location=location,
            company=company
        )

        return redirect('overview')  # Redirect to the overview page for money transfer transactions

    template = 'ui/mt_rec.html'  
    return render(request, template)