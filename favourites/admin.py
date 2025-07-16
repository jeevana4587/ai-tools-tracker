from django.contrib import admin
from .models import Favourites
@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'tool', 'added_on')
    search_fields = ('user__username', 'tool__name')
    list_filter = ('added_on',)