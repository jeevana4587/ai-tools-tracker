from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import HelpContent, UserSettings, UserProfile
from .forms import UserSettingsForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:dashboard')
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, form.get_user())
            return redirect('dashboard:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_settings_view(request):
    settings, created = UserSettings.objects.get_or_create(user=request.user)
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
    # Get or create user profile
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
            'email': request.user.email
        }
    )
    
    # Get user settings for theme
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    
    context = {
        'profile': profile,
        'user_settings': user_settings,
        'user_theme': user_settings.theme
    }
    return render(request, 'users/profile.html', context)

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('users:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    
    # Get user settings for theme
    user_settings, created = UserSettings.objects.get_or_create(user=request.user)
    
    context = {
        'form': form,
        'user_theme': user_settings.theme
    }
    return render(request, 'users/change_password.html', context)