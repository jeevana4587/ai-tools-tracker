from django.shortcuts import render
from tools.models import Tool, Category
from reviews.models import Review
from history.models import ToolHistory
from favourites.models import Favourites
from django.db.models import Avg, Count, Q
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import pprint

def analytics_dashboard(request):
    # Get all categories and create charts for each
    categories = Category.objects.all()
    category_charts = []

    for category in categories:
        tools = Tool.objects.filter(category=category)
        
        if tools.exists():
            # Get tools with their average ratings
            tools_with_ratings = (
                tools.annotate(avg_rating=Avg('reviews__stars'))
                .values('name', 'avg_rating')
                .filter(avg_rating__isnull=False)
            )
            
            if tools_with_ratings.exists():
                # Use actual ratings for pie chart
                chart_data = list(tools_with_ratings)
            else:
                # If no reviews, use tool count as data (for visualization)
                chart_data = [{'name': tool.name, 'avg_rating': 1} for tool in tools[:5]]
        else:
            # If no tools in category, create placeholder data
            chart_data = [{'name': 'No tools yet', 'avg_rating': 1}]

        category_charts.append({
            'category_name': category.name,
            'tools': chart_data,
            'chart_type': 'pie',
            'tool_count': tools.count(),
            'has_reviews': tools_with_ratings.exists() if tools.exists() else False
        })

    # Enhanced Analytics Data
    analytics_data = {
        'category_charts': category_charts,
        
        # Overall Statistics
        'total_tools': Tool.objects.count(),
        'total_categories': Category.objects.count(),
        'total_reviews': Review.objects.count(),
        'total_users': User.objects.count(),
        
        # Rating Statistics
        'avg_overall_rating': Review.objects.aggregate(avg=Avg('stars'))['avg'] or 0,
        'total_rated_tools': Tool.objects.filter(reviews__isnull=False).distinct().count(),
        
        # Top Rated Tools
        'top_rated_tools': Tool.objects.annotate(
            avg_rating=Avg('reviews__stars'),
            review_count=Count('reviews')
        ).filter(avg_rating__isnull=False).order_by('-avg_rating')[:10],
        
        # Category Statistics
        'category_stats': Category.objects.annotate(
            tool_count=Count('tool'),
            avg_rating=Avg('tool__reviews__stars')
        ).order_by('-tool_count'),
        
        # Access Type Distribution
        'access_type_stats': Tool.objects.values('access_type').annotate(
            count=Count('id')
        ).order_by('-count'),
        

    }

    return render(request, 'analytics/analytics_dashboard.html', analytics_data)
