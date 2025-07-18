from django.urls import path
from . import views
from .views import homepage_view, categories_view

app_name = 'tools'

urlpatterns = [
    path('', homepage_view, name='home'),
    path('list/', views.tools_list, name='list'),
    path('categories/', categories_view, name='categories'),
    path('category/<int:category_id>/', views.tools_by_category, name='by_category'),
    path('tool/<int:tool_id>/', views.tool_detail, name='tool_detail'),
    path('all-categories/', views.all_categories, name='all_categories'),
]