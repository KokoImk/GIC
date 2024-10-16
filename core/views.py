from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from core.models import *

from .forms import AdminSignUpForm, CustomerSignUpForm

# third party login
from social_django.views import auth, complete
from social_core.exceptions import AuthCanceled

from django_countries import countries

def admin_signup(request):

    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = True
            user.is_staff = True
            user.is_active = True
            user.is_superuser = True
            user.save()
            return redirect('core:login')
    else:
        form = AdminSignUpForm()
    return render(request, 'accounts/admin-register.html', {'form': form })


def applicant_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_applicant = True
            user.save()
            return redirect('core:login')
    else:
        form = CustomerSignUpForm()
    return render(request, 'accounts/register.html', {'form': form })


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect.')
            return redirect('core:login')

    # If GET request or POST request failed authentication
    context = {}
    return render(request, 'accounts/login.html', context)



# Handling auth for google
def google_login(request):
    # Redirect users to Google's login page
    return auth(request, 'google-oauth2')

def google_complete(request):
    # Handle the authentication callback from Google
    try:
        response = complete(request, 'google-oauth2')
    except AuthCanceled:
        # Handle case where authentication is canceled
        return HttpResponseBadRequest("Authentication Canceled")
    return response


# Logout
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('core:login')
