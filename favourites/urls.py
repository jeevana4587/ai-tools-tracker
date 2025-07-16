from django.urls import path
from . import views

app_name = 'favourites'

urlpatterns = [
    path('', views.favourites_list, name='list'),
    path('toggle/<int:tool_id>/', views.toggle_favourite, name='toggle'),
]
