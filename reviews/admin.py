from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'tool', 'stars', 'created_at')
    list_filter = ('stars', 'created_at')
