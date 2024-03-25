#!/usr/bin/python3.12
"""Defines URL patterns for site surveys."""
from django.urls import path

from . import views


app_name = "site_surveys"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Page that shows all sites.
    path("sites/", views.sites, name="sites"),
    # Detail page for a single site.
    path("sites/<int:site_id>/", views.site, name="site"),
    # Page for adding a new site.
    path("new_site/", views.new_site, name="new_site"),
    # Page for editing an entry.
    path("edit_site/<int:site_id>/", views.edit_site, name="edit_site"),
    path('export_csv', views.export_csv, name='exportcsv')
]
