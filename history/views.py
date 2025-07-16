from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import ToolHistory
from tools.models import Tool
from django.contrib.auth.decorators import login_required

@login_required
def view_history(request):
    history = request.user.tool_history.select_related('tool').order_by('-accessed_at')
    return render(request, 'history/view_history.html', {'history': history})
