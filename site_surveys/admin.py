#!/usr/bin/python3.12
from django.contrib import admin

from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "site_type", "date_added", "updated")
    list_filter = ["owner", "site_type", "date_added", "updated"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["owner"]
    date_hierarchy = "updated"
    ordering = ["updated"]
