from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('add/<int:tool_id>/', views.add_review, name='add_review'),
    path('', views.reviews_dashboard, name='dashboard'), 
    path('<int:tool_id>/', views.tool_reviews, name='tool_reviews'), 
]
