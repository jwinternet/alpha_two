#!/usr/bin/python3.12
from django.contrib import admin

from .models import Site


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("title", "site_type", "owner", "address")
    list_filter = ["date_added", "owner"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["owner"]
    date_hierarchy = "updated"
    ordering = ["updated"]
