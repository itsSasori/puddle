from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from . import views
from .forms import LoginForm

urlpatterns=[
    path('register/',views.register,name='register'),
    path('logout/',views.Logout,name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html', authentication_form=LoginForm), name='login'),  
]