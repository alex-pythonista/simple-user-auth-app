from django.shortcuts import render

# Create your views here.

# home URL
def home(request):
    
    context = {}
    template_name = 'loginApp/home.html'

    return render(request, template_name, context)