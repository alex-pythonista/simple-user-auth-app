from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


from .models import UserProfile
from core.views import home
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

        return HttpResponseRedirect(reverse('loginApp:login'))

    else:    
        context = {}
        template_name = 'loginApp/register.html'
        return render(request, template_name, context)


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse(home))
             
        else:
            return HttpResponse("invalid login information!")

    else:
        context = {}
        template_name = 'loginApp/login.html'
        return render(request, template_name, context)