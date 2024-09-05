from django.contrib import admin
from .models import User

from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name','first_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('eamil',)

admin.site.register(User, UserAdmin)



