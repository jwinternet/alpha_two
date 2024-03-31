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
    path("about/", views.about, name="about"),
    # Detail page for a single site.
    path("sites/<int:site_id>/", views.site, name="site"),
    # Page for adding a new site.
    path("new_site/", views.new_site, name="new_site"),
    # Page for editing an entry.
    path("edit_site/<int:site_id>/", views.edit_site, name="edit_site"),
    path("photo_checklist/<int:site_id>/", views.photo_checklist, name="photo_checklist"),
    path("network_checklist/<int:site_id>/", views.network_checklist, name="network_checklist"),
    path("server_checklist/<int:site_id>/", views.server_checklist, name="server_checklist"),
    path("mdf_checklist/<int:site_id>/", views.mdf_checklist, name="mdf_checklist"),
    path("idf_checklist/<int:site_id>/", views.idf_checklist, name="idf_checklist"),
    path('export_all_sites/', views.export_all_sites, name='export_all_sites'),
    path('export_site/<int:site_id>/', views.export_site, name='export_site'),
    path('download_file/<int:site_id>/', views.download_file, name='download_file'),
    path('search_results/', views.SearchResultsView.as_view(), name='search_results'),
]
