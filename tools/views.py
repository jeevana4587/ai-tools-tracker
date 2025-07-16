from django.shortcuts import render, get_object_or_404
from .models import Tool, Category
from django.db.models import Count
from history.models import ToolHistory
from favourites.models import Favourites 
from history.models import ToolHistory


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'tools/categories_list.html', {'categories': categories})

def tools_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        tools = Tool.objects.filter(category_id=category_id)
    else:
        tools = Tool.objects.all()

    return render(request, 'tools/tools_list.html', {
        'tools': tools,
        'categories': categories
    })

def tools_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tools = Tool.objects.filter(category=category)
    return render(request, 'tools/tools_by_category.html', {'category': category, 'tools': tools})

def tool_detail(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    
    if request.user.is_authenticated:
        ToolHistory.objects.create(user=request.user, tool=tool)

    return render(request, 'tools/tool_detail.html', {'tool': tool})

    is_favourited = False
    if request.user.is_authenticated:
        is_favourited = Favourites.objects.filter(user=request.user, tool=tool).exists()

    context = {
        'tool': tool,
        'is_favourited': is_favourited,
    }

    if request.headers.get('Hx-Request') == 'true':
        return render(request, 'tools/partials/tool_detail_partial.html', context)
    
    return render(request, 'tools/tool_detail.html', context)
    
def all_categories(request):
    categories = Category.objects.all()
    return render(request, 'tools/all_categories.html', {'categories': categories})

def homepage_view(request):
    tools = Tool.objects.annotate(num_reviews=Count('reviews')).order_by('-num_reviews')[:6]
    return render(request, 'tools/homepage.html', {'tools': tools})