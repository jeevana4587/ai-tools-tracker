from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, UserSettings

@receiver(post_save, sender=User)
def create_user_profile_and_settings(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, name=instance.username, email=instance.email)
        UserSettings.objects.create(user=instance)
