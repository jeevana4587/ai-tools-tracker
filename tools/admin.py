from django.contrib import admin
from .models import Category, Tool

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'website','access_type']
    search_fields = ['name', 'description']
    list_filter = ['category','access_type']
