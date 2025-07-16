from django.shortcuts import render
from tools.models import Tool, Category
from reviews.models import Review
from django.db.models import Avg
import pprint

def analytics_dashboard(request):
    categories = Category.objects.all()
    category_charts = []

    for category in categories:
        tools = (
            Tool.objects.filter(category=category)
            .annotate(avg_rating=Avg('reviews__rating'))
            .values('name', 'avg_rating')
        )

        
        if not tools:
            continue

        chart_type = 'bar' if len(tools) > 5 else 'pie'

        category_charts.append({
            'category_name': category.name,
            'tools': list(tools),
            'chart_type': chart_type
        })
    pprint.pprint(category_charts)
    return render(request, 'analytics/analytics_dashboard.html', {
        'category_charts': category_charts
    })
