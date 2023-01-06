from django.contrib import admin


class ActivationCodeAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'type']
    search_fields = ['user']

