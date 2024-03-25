#!/usr/bin/python3.12
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import csv

from .models import Site
from .forms import SiteForm


def index(request):
    """The home page for Site Surveys."""
    return render(request, "site_surveys/index.html")


@login_required
def sites(request):
    """Show all sites."""
    sites = Site.objects.order_by("date_added")

    # Pagination with 3 posts per page
    paginator = Paginator(sites, 5)
    page_number = request.GET.get("page", 1)
    try:
        site = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        site = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        site = paginator.page(paginator.num_pages)
    context = {"sites": site}
    return render(request, "site_surveys/sites.html", context)


@login_required
def site(request, site_id):
    """Show a single site and all of its notes."""
    try:
        # site = Site.objects.get(id=site_id)
        site = get_object_or_404(Site, id=site_id)
        # # Make sure the site belongs to the current user.
        # if site.owner != request.user:
        #     raise Http404

        context = {
            "site": site
        }
        return render(request, "site_surveys/site.html", context)

    except:
        return redirect("site_surveys:sites")


@login_required
def new_site(request):
    """Add a new site."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = SiteForm()
    else:
        # POST data submitted; process data.
        form = SiteForm(data=request.POST)
        if form.is_valid():
            new_site = form.save(commit=False)
            new_site.owner = request.user
            new_site.save()
            return redirect("site_surveys:sites")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "site_surveys/new_site.html", context)


@login_required
def edit_site(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = SiteForm(instance=site)
    else:
        # POST data submitted; process data.
        form = SiteForm(instance=site, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("site_surveys:sites")

    # Display a blank or invalid form.
    context = {"site": site, "form": form}
    return render(request, "site_surveys/edit_site.html", context)


@login_required
def export_all_sites(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_all_sites.csv"'
    export_sites = Site.objects.all()

    writer = csv.writer(response)
    writer.writerow(["title", "text", "first_name", "last_name", "email", "age", "site_type"])

    for export_site in export_sites:
        writer.writerow([
            export_site.title,
            export_site.text,
            export_site.first_name,
            export_site.last_name,
            export_site.email,
            export_site.age,
            export_site.site_type,
        ])
    return response


@login_required
def export_site(request, site_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_site.csv"'
    export_site = get_object_or_404(Site, id=site_id)

    writer = csv.writer(response)
    writer.writerow(["title", "text", "first_name", "last_name", "email", "age", "site_type"])

    writer.writerow([
        export_site.title,
        export_site.text,
        export_site.first_name,
        export_site.last_name,
        export_site.email,
        export_site.age,
        export_site.site_type,
    ])
    return response
