#!/usr/bin/python3.12
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Site
from .forms import SiteForm


def index(request):
    """The home page for Site Surveys."""
    return render(request, "site_surveys/index.html")


@login_required
def sites(request):
    """Show all sites."""
    sites = Site.objects.filter(owner=request.user).order_by("date_added")
    # Pagination with 3 posts per page
    paginator = Paginator(sites, 10)
    page_number = request.GET.get("page", 1)
    try:
        site = paginator.page(page_number)
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
        site = get_object_or_404(
            Site,
            id=site_id
        )
        # Make sure the site belongs to the current user.
        if site.owner != request.user:
            raise Http404

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
    edit_site = Site.objects.get(id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = SiteForm(instance=edit_site)
    else:
        # POST data submitted; process data.
        form = SiteForm(instance=edit_site, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("site_surveys:sites", site_id=edit_site)

    # Display a blank or invalid form.
    context = {"site": edit_site, "form": form}
    return render(request, "site_surveys/edit_site.html", context)
