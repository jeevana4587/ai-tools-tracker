from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),
    path('categories/', views.categories_view, name='categories'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('favourites/', views.favourites_view, name='favourites'),
    path('history/', views.history_view, name='history'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('tool-of-the-day/', views.tool_of_day_view, name='tool_of_day'),
    path('profile/', views.profile_view, name='profile'),
    path('settings/', views.settings_view, name='settings'),
]


