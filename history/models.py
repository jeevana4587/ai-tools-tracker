from django.db import models
from django.contrib.auth.models import User
from tools.models import Tool

class ToolHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tool_history')
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    accessed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} viewed {self.tool.name} on {self.accessed_at}"

    class Meta:
        ordering = ['-accessed_at']  
        verbose_name = "Tool History"
        verbose_name_plural = "Tool History"
