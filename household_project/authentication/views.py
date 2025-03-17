from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Fixed email and password
VALID_EMAIL = 'rhu_rizal@google.com'
VALID_PASSWORD = 'rizalRHU2025'

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == VALID_EMAIL and password == VALID_PASSWORD:
            return redirect('dashboard:index')

        return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})

    return render(request, 'authentication/login.html')

def logout_view(request):
    return redirect('login')

# Create your views here.
