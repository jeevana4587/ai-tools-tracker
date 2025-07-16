from django.contrib import admin
from .models import Review, ReviewHelpfulVote, ReviewReport

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'tool', 'stars', 'title', 'is_verified', 'is_featured', 'is_approved', 'helpful_votes_count', 'created_at')
    list_filter = ('stars', 'is_verified', 'is_featured', 'is_approved', 'created_at', 'tool__category')
    search_fields = ('user__username', 'tool__name', 'title', 'comment')
    readonly_fields = ('created_at', 'updated_at', 'helpful_votes_count', 'not_helpful_votes_count', 'helpful_score')
    list_editable = ('is_verified', 'is_featured', 'is_approved')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'tool', 'stars', 'title')
        }),
        ('Review Content', {
            'fields': ('comment', 'pros', 'cons')
        }),
        ('Status', {
            'fields': ('is_verified', 'is_featured', 'is_approved')
        }),
        ('Statistics', {
            'fields': ('helpful_votes_count', 'not_helpful_votes_count', 'helpful_score'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    actions = ['approve_reviews', 'feature_reviews', 'verify_reviews']
    
    def approve_reviews(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} reviews approved.')
    approve_reviews.short_description = 'Approve selected reviews'
    
    def feature_reviews(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} reviews featured.')
    feature_reviews.short_description = 'Feature selected reviews'
    
    def verify_reviews(self, request, queryset):
        updated = queryset.update(is_verified=True)
        self.message_user(request, f'{updated} reviews verified.')
    verify_reviews.short_description = 'Verify selected reviews'

@admin.register(ReviewHelpfulVote)
class ReviewHelpfulVoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'is_helpful', 'created_at')
    list_filter = ('is_helpful', 'created_at')
    search_fields = ('review__tool__name', 'user__username')

@admin.register(ReviewReport)
class ReviewReportAdmin(admin.ModelAdmin):
    list_display = ('review', 'reporter', 'reason', 'is_resolved', 'created_at')
    list_filter = ('reason', 'is_resolved', 'created_at')
    search_fields = ('review__tool__name', 'reporter__username', 'description')
    list_editable = ('is_resolved',)
    
    fieldsets = (
        ('Report Information', {
            'fields': ('review', 'reporter', 'reason', 'description')
        }),
        ('Status', {
            'fields': ('is_resolved',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        })
    )
    
    actions = ['mark_resolved']
    
    def mark_resolved(self, request, queryset):
        updated = queryset.update(is_resolved=True)
        self.message_user(request, f'{updated} reports marked as resolved.')
    mark_resolved.short_description = 'Mark selected reports as resolved'
