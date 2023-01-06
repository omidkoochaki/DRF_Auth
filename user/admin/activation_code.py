from django.contrib import admin


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'type', 'created_at']
    search_fields = ['user']

