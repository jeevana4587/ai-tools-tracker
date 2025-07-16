from django.shortcuts import render
from favourites.models import Favourites
from tools.models import Tool

def dashboard_home(request):
    tools = Tool.objects.all()
    return render(request, 'dashboard/home.html', {'tools': tools})

def dashboard_view(request):
    return render(request, 'dashboard/base.html')


def categories_view(request):
    return render(request, 'dashboard/categories.html')

def reviews_view(request):
    return render(request, 'dashboard/reviews.html')


def favourites_view(request):
    favourites = Favourites.objects.filter(user=request.user).select_related('tool')
    return render(request, 'dashboard/favourites.html', {'favourites': favourites})

def history_view(request):
    return render(request, 'dashboard/history.html')

def feedback_view(request):
    return render(request, 'dashboard/feedback.html')

def tool_of_day_view(request):
    return render(request, 'dashboard/tool_of_day.html')

def profile_view(request):
    return render(request, 'dashboard/profile.html')

def settings_view(request):
    return render(request, 'dashboard/settings.html')
