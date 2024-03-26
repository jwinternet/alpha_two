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
    path("useful_links/", views.useful_links, name="useful_links"),
    path("documentation/", views.documentation, name="documentation"),
    path("contacts/", views.contacts, name="contacts"),
    # Detail page for a single site.
    path("sites/<int:site_id>/", views.site, name="site"),
    # Page for adding a new site.
    path("new_site/", views.new_site, name="new_site"),
    # Page for editing an entry.
    path("edit_site/<int:site_id>/", views.edit_site, name="edit_site"),
    path('export_all_sites/', views.export_all_sites, name='export_all_sites'),
    path('export_site/<int:site_id>/', views.export_site, name='export_site')
]
