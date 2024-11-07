# admin.py
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "message",
        "created_at",
    )  # Display these fields in the admin list view
    search_fields = (
        "name",
        "email",
        "phone",
    )  # Enable search functionality on these fields
    list_filter = ("created_at",)  # Filter by creation date
    readonly_fields = ("created_at",)  # Make the created_at field read-only


# Register the Contact model with the custom admin class
admin.site.register(Contact, ContactAdmin)
