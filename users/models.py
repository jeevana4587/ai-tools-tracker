from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"



class UserSettings(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('te', 'Telugu'),
    ]

    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default='light')
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')

    def __str__(self):
        return f"{self.user.username}'s Settings"

    class Meta:
        verbose_name = "User Settings"
        verbose_name_plural = "User Settings"



class HelpContent(models.Model):
    LANGUAGE_CHOICES = UserSettings.LANGUAGE_CHOICES  

    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')
    content = models.TextField()

    def __str__(self):
        return f"Help Content ({self.get_language_display()})"

    class Meta:
        verbose_name = "Help Content"
        verbose_name_plural = "Help Contents"
