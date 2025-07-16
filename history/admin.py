from django.contrib import admin
from .models import ToolHistory

@admin.register(ToolHistory)
class ToolHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'tool', 'accessed_at']
    search_fields = ['user__username', 'tool__name']
    list_filter = ['accessed_at']
