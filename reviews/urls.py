from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    # Dashboard and overview
    path('', views.reviews_dashboard, name='dashboard'), 
    path('analytics/', views.review_analytics, name='analytics'),
    path('my-reviews/', views.my_reviews, name='my_reviews'),
    
    # Tool reviews
    path('tool/<int:tool_id>/', views.tool_reviews, name='tool_reviews'), 
    
    # Review CRUD operations
    path('add/<int:tool_id>/', views.add_review, name='add_review'),
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    
    # Review interactions
    path('vote-helpful/<int:review_id>/', views.vote_helpful, name='vote_helpful'),
    path('report/<int:review_id>/', views.report_review, name='report_review'),
]
