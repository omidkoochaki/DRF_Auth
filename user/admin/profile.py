from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_name']
    search_fields = ['user']
