from django.contrib import admin

from scrapper.models.user import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
