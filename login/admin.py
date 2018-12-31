from django.contrib import admin

# Register your models here.

from .models import (
    Profiles,
    ProfilesBank,
)


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    pass

@admin.register(ProfilesBank)
class ProfilesBankAdmin(admin.ModelAdmin):
    pass