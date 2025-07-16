from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'rating', 'submitted_at', 'resolved']
    list_filter = ['resolved', 'submitted_at', 'rating']
    search_fields = ['subject', 'message', 'user__username']
