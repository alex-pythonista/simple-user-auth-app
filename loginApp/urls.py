from django.urls import path
from . import views

app_name = 'loginApp'

urlpatterns = [
    path('register/', views.register, name='register'),
    
]