from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

# home URL
@login_required
def home(request):
    
    context = {}
    template_name = 'loginApp/home.html'

    return render(request, template_name, context)