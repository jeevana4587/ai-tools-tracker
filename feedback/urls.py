from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('submit/', views.submit_feedback, name='submit_feedback'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]
