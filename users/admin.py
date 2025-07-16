from django.contrib import admin
from .models import UserProfile, UserSettings, HelpContent

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')

@admin.register(UserSettings)
class UserSettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'theme', 'language')

@admin.register(HelpContent)
class HelpContentAdmin(admin.ModelAdmin):
    list_display = ('language',)
