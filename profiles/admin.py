from django.contrib import admin

# Register your models here.

from .models import *

class RelationAdminTab(admin.TabularInline):
    model = Address
    fields = [
        'address'
    ]

    def has_delete_permission(self, *args, **kwargs):
         return False

class UserProfileAdmin(admin.ModelAdmin):

    inlines = [
        RelationAdminTab,
    ]

    list_display =[
        'fullname',
        'active',
        'lastupdate',
        'balance',
        'age',
        "gotoGoogle"
    ]
    list_display_links =[
        'balance'
    ]
    search_fields = [
        'fullname'
    ]
    list_filter = [
        'gender'
    ]
    
    def get_readonly_fields(self, request, obj, *args, **kwargs):
        if obj:
            return [
                "fullname"
            ]
        else:
            return []

    # def has_add_permission(self, *args, **kwargs):
    #     return False

    # def has_delete_permission(self, *args, **kwargs):
    #     return False

    # def has_change_permission(self, *args, **kwargs):
    #     return False

    # def has_view_permission(self, *args, **kwargs):
    #     return False



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Relation)
