from django.urls import path
from . import views
from core.views import home

app_name = 'loginApp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('index/', home, name='home')
    
]