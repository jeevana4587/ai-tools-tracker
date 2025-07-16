from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from tools.models import Tool
from .models import Favourites

@login_required
def favourites_list(request):
    favourites = Favourites.objects.filter(user=request.user).select_related('tool')
    return render(request, 'favourites/favourites_list.html', {'favourites': favourites})

@login_required
def toggle_favourite(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    favourite, created = Favourites.objects.get_or_create(user=request.user, tool=tool)

    if not created:
        favourite.delete()
    return redirect('dashboard:favourites')

