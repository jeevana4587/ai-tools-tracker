from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, related_name='favourited_by')
    added_on = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255, blank=True, help_text="Optional note about why you favorited this tool")

    class Meta:
        unique_together = ('user', 'tool')  
        ordering = ['-added_on']

    def __str__(self):
        return f"{self.user.username} - {self.tool.name}"

    class Meta:
        verbose_name = "Favourites"
        verbose_name_plural = "Favourites"
