from django.shortcuts import render

from django.contrib.auth.models import User
from .models import UserProfile

# Create your views here.

def register(request):

    context = {}
    template_name = 'loginApp/register.html'
    return render(request, template_name, context)