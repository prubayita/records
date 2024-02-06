from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .decorators import *
from .models import *
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def login(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('bank_overview')  # Redirect to the desired page after successful login
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

# def bank_overview(request):
#     # Get filter parameters from GET request
#     bank_name = request.GET.get('bank_name')
#     transaction_type = request.GET.get('transaction_type')
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     # Get all transactions by default
#     transactions = BankTransaction.objects.all()

#     # Apply filters based on parameters
#     if bank_name:
#         transactions = transactions.filter(bank_name=bank_name)
#     if transaction_type:
#         transactions = transactions.filter(transaction_type=transaction_type)
#     if start_date:
#         transactions = transactions.filter(date__gte=start_date)
#     if end_date:
#         transactions = transactions.filter(date__lte=end_date)
    
#     total_amount = transactions.aggregate(Sum('amount'))['amount__sum']

#     template = 'ui/test2.html'
#     context = {'transactions': transactions, 'total_amount': total_amount}
#     return render(request, template, context)
@login_required
@group_required('Supervisor')
def bank_overview(request):
    bank_name = request.GET.get('bank_name')
    transaction_type = request.GET.get('transaction_type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    transactions = BankTransaction.objects.all()

    if bank_name:
        transactions = transactions.filter(bank_name=bank_name)
    if transaction_type:
        transactions = transactions.filter(transaction_type=transaction_type)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(transactions, 10)  # Show 10 transactions per page

    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)

    total_amount = transactions.object_list.aggregate(Sum('amount'))['amount__sum']

    template = 'ui/test2.html'
    context = {'transactions': transactions, 'total_amount': total_amount}
    return render(request, template, context)

# def mt_overview(request):
#     # Get filter parameters from GET request
#     company = request.GET.get('company')
#     sender_name = request.GET.get('sender_name')
#     transaction_type = request.GET.get('transaction_type')
#     start_date = request.GET.get('start_date')
#     end_date = request.GET.get('end_date')

#     # Get all money transfer transactions by default
#     transactions = MoneyTransferTransaction.objects.all()

#     # Apply filters based on parameters
#     if company:
#         transactions = transactions.filter(company=company)
#     if sender_name:
#         transactions = transactions.filter(sender_name=sender_name)
#     if transaction_type:
#         transactions = transactions.filter(transaction_type=transaction_type)
#     if start_date:
#         transactions = transactions.filter(date__gte=start_date)
#     if end_date:
#         transactions = transactions.filter(date__lte=end_date)

#     total_amount = transactions.aggregate(Sum('amount'))['amount__sum']

#     template = 'ui/mt_overview.html'  # Adjust the template path accordingly
#     context = {'transactions': transactions, 'total_amount': total_amount}
#     return render(request, template, context)
@login_required
def mt_overview(request):
    # Get filter parameters from GET request
    company = request.GET.get('company')
    sender_name = request.GET.get('sender_name')
    transaction_type = request.GET.get('transaction_type')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Get all money transfer transactions by default
    transactions = MoneyTransferTransaction.objects.all()

    # Apply filters based on parameters
    if company:
        transactions = transactions.filter(company=company)
    if sender_name:
        transactions = transactions.filter(sender_name=sender_name)
    if transaction_type:
        transactions = transactions.filter(transaction_type=transaction_type)
    if start_date:
        transactions = transactions.filter(date__gte=start_date)
    if end_date:
        transactions = transactions.filter(date__lte=end_date)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(transactions, 10)  # Show 10 transactions per page

    try:
        transactions = paginator.page(page)
    except PageNotAnInteger:
        transactions = paginator.page(1)
    except EmptyPage:
        transactions = paginator.page(paginator.num_pages)

    total_amount = transactions.object_list.aggregate(Sum('amount'))['amount__sum']

    template = 'ui/mt_overview.html'  # Adjust the template path accordingly
    context = {'transactions': transactions, 'total_amount': total_amount}
    return render(request, template, context)

@login_required
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

        return redirect('bank_record')  # Redirect to the overview page or any other page

    template = 'ui/rec.html'
    return render(request, template)
@login_required
def mt_record(request):
    if request.method == 'POST':
        # Retrieve data from the form
        sender_name = request.POST.get('sender_name')
        sender_id_passport = request.POST.get('sender_id_passport')
        transaction_type = request.POST.get('transaction_type')
        location = request.POST.get('location')
        company = request.POST.get('company')
        amount = request.POST.get('amount')

        # Create a new MoneyTransferTransaction instance and save it
        MoneyTransferTransaction.objects.create(
            sender_name=sender_name,
            sender_id_passport=sender_id_passport,
            transaction_type=transaction_type,
            location=location,
            company=company,
            amount=amount
        )

        return redirect('mt_record')  # Redirect to the overview page for money transfer transactions

    template = 'ui/mt_rec.html'  
    return render(request, template)



def user_list(request):
    users = User.objects.all()
    return render(request, 'ui/user_list.html', {'users': users})

def delete_user(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            messages.success(request, f"User '{user.username}' has been deleted.")
        except User.DoesNotExist:
            messages.error(request, "User not found.")
    return redirect('user_list')

def approve_staff(request, user_id):
    if request.method == 'POST':
        try:
            user = User.objects.get(id=user_id)
            user.is_staff = True
            user.save()
            messages.success(request, f"Staff status for '{user.username}' has been approved.")
        except User.DoesNotExist:
            messages.error(request, "User not found.")
    return redirect('user_list')