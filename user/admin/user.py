from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ['mobile', 'email', 'is_mobile_verified', 'is_email_verified']
    search_fields = ['email', 'mobile']
