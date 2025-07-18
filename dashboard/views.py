from django.shortcuts import render, redirect
from favourites.models import Favourites
from tools.models import Tool, Category

def dashboard_home(request):
    tools = Tool.objects.all()
    return render(request, 'dashboard/home.html', {'tools': tools})

def dashboard_view(request):
    return render(request, 'dashboard/base.html')

def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories_bubbles.html', {'categories': categories})

def reviews_view(request):
    return redirect('reviews:dashboard')

def favourites_view(request):
    return redirect('favourites:list')

def history_view(request):
    return redirect('history:list')

def feedback_view(request):
    return redirect('feedback:submit_feedback')

def tool_of_day_view(request):
    # Implement logic or redirect as needed
    return render(request, 'dashboard/tool_of_day.html')

def profile_view(request):
    return redirect('users:profile')

def settings_view(request):
    return redirect('users:settings')
