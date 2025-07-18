from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool  

class Review(models.Model):
    RATING_CHOICES = [(i, f"{i}★") for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tool')
        ordering = ['-created_at']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.user.username} - {self.tool.name} ({self.stars}★)"