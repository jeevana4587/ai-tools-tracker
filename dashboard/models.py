from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool

class DashboardAnalytics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="dashboard_analytics")
    total_tools_viewed = models.PositiveIntegerField(default=0)
    total_reviews_given = models.PositiveIntegerField(default=0)
    total_favourites = models.PositiveIntegerField(default=0)
    total_feedbacks = models.PositiveIntegerField(default=0)
    last_login_time = models.DateTimeField(null=True, blank=True)
    last_active_tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Dashboard Analytics"

    class Meta:
        verbose_name = "Favourites"
        verbose_name_plural = "Favourites"


class ToolOfTheDay(models.Model):
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    date = models.DateField(unique=True)

    def __str__(self):
        return f"Tool of {self.date}: {self.tool.name}"

    class Meta:
        verbose_name = "Favourites"
        verbose_name_plural = "Favourites"

