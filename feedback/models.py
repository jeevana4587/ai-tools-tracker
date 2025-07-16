from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    subject = models.CharField(max_length=255)
    message = models.TextField()

    rating = models.IntegerField(
        choices=[
            (1, '1 - Very Poor'),
            (2, '2 - Poor'),
            (3, '3 - Average'),
            (4, '4 - Good'),
            (5, '5 - Excellent'),
        ],
        null=True,
        blank=True
    )

    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedback"

    def __str__(self):
        return f"Feedback from {self.user.username if self.user else 'Anonymous'}"

