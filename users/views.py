from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import HelpContent, UserSettings
from .forms import UserSettingsForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_settings_view(request):
    settings = request.user.usersettings
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, instance=settings)
        if form.is_valid():
            form.save()
            return redirect('dashboard:settings')
    else:
        form = UserSettingsForm(instance=settings)
    return render(request, 'users/settings.html', {'form': form})

@login_required
def help_view(request):
    language = 'en'
    if request.user.is_authenticated:
        user_settings = UserSettings.objects.filter(user=request.user).first()
        if user_settings:
            language = user_settings.language

    help_text = HelpContent.objects.filter(language=language).first()
    return render(request, 'users/help.html', {'help_text': help_text})

@login_required
def profile_view(request):
    profile = request.user.userprofile
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})