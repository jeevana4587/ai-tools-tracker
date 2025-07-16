from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    RATING_CHOICES = [(i, f"{i}★") for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(
        choices=RATING_CHOICES,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)
    
    # Enhanced fields
    title = models.CharField(max_length=200, blank=True, help_text="Brief title for your review")
    pros = models.TextField(blank=True, help_text="What you liked about this tool")
    cons = models.TextField(blank=True, help_text="What could be improved")
    
    # Verification and moderation
    is_verified = models.BooleanField(default=False, help_text="Verified user review")
    is_featured = models.BooleanField(default=False, help_text="Featured review")
    is_approved = models.BooleanField(default=True, help_text="Review approved by moderators")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'tool')
        ordering = ['-created_at']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.user.username} - {self.tool.name} ({self.stars}★)"
    
    @property
    def helpful_votes_count(self):
        return self.helpful_votes.filter(is_helpful=True).count()
    
    @property
    def not_helpful_votes_count(self):
        return self.helpful_votes.filter(is_helpful=False).count()
    
    @property
    def helpful_score(self):
        helpful = self.helpful_votes_count
        not_helpful = self.not_helpful_votes_count
        total = helpful + not_helpful
        if total == 0:
            return 0
        return (helpful / total) * 100

class ReviewHelpfulVote(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='helpful_votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_helpful = models.BooleanField()  # True for helpful, False for not helpful
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('review', 'user')
        verbose_name = "Helpful Vote"
        verbose_name_plural = "Helpful Votes"

    def __str__(self):
        vote_type = "Helpful" if self.is_helpful else "Not Helpful"
        return f"{self.user.username} - {vote_type} for {self.review}"

class ReviewReport(models.Model):
    REPORT_REASONS = [
        ('inappropriate', 'Inappropriate Content'),
        ('spam', 'Spam'),
        ('fake', 'Fake Review'),
        ('offensive', 'Offensive Language'),
        ('other', 'Other'),
    ]
    
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='reports')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REPORT_REASONS)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('review', 'reporter')
        verbose_name = "Review Report"
        verbose_name_plural = "Review Reports"

    def __str__(self):
        return f"Report: {self.review} - {self.reason}"