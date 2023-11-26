from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.models import User, Group
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


def overview(request):
  template = loader.get_template('ui/test2.html')
  return HttpResponse(template.render())