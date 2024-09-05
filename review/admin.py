from django.contrib import admin


from .models import Favorite


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at', 'user')
    search_fields = ('user',)
