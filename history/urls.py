from django.urls import path
from . import views

app_name = 'history'

urlpatterns = [
    path('', views.view_history, name='list'),
]
