from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

def register(request):

    registered = False

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        user_obj = User(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()


    context = {}
    template_name = 'loginApp/register.html'
    return render(request, template_name, context)


def login_user(request):


    context = {}
    template_name = 'loginApp/login.html'
    return render(request, template_name, context)