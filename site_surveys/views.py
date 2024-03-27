#!/usr/bin/python3.12
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from csv import writer

from .models import Site
from .forms import SiteForm, PhotoForm, NetworkForm, ServerForm, MDFForm, IDFForm


def index(request):
    """The home page for Site Surveys."""
    return render(request, "site_surveys/index.html")


@login_required
def sites(request):
    """Show all sites."""
    sites = Site.objects.order_by("date_added")

    # Pagination with 3 posts per page
    paginator = Paginator(sites, 10)
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
        site_form = SiteForm()
    else:
        # POST data submitted; process data.
        site_form = SiteForm(data=request.POST)
        if site_form.is_valid():
            new_site = site_form.save(commit=False)
            new_site.owner = request.user
            new_site.save()
            return redirect("site_surveys:sites")

    # Display a blank or invalid form.
    context = {"site_form": site_form}
    return render(request, "site_surveys/new_site.html", context)


@login_required
def edit_site(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        site_form = SiteForm(instance=site)

    else:
        # POST data submitted; process data.
        site_form = SiteForm(instance=site, data=request.POST)
        if site_form.is_valid():
            site_form.save()
            context = {"site": site}
            return render(request, "site_surveys/site.html", context)

    # Display a blank or invalid form.
    context = {"site": site, "site_form": site_form}
    return render(request, "site_surveys/edit_site.html", context)


@login_required
def photo_checklist(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        photo_form = PhotoForm(instance=site)

    else:
        # POST data submitted; process data.
        photo_form = PhotoForm(instance=site, data=request.POST)
        if photo_form.is_valid():
            photo_form.save()
            context = {"site": site}
            return render(request, "site_surveys/site.html", context)

    # Display a blank or invalid form.
    context = {"site": site, "photo_form": photo_form}
    return render(request, "site_surveys/photo_checklist.html", context)


@login_required
def network_checklist(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        network_form = NetworkForm(instance=site)

    else:
        # POST data submitted; process data.
        network_form = NetworkForm(instance=site, data=request.POST)
        if network_form.is_valid():
            network_form.save()
            context = {"site": site}
            return render(request, "site_surveys/site.html", context)

    # Display a blank or invalid form.
    context = {"site": site, "network_form": network_form}
    return render(request, "site_surveys/network_checklist.html", context)


@login_required
def server_checklist(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        server_form = ServerForm(instance=site)

    else:
        # POST data submitted; process data.
        server_form = ServerForm(instance=site, data=request.POST)
        if server_form.is_valid():
            server_form.save()
            context = {"site": site}
            return render(request, "site_surveys/site.html", context)

    # Display a blank or invalid form.
    context = {"site": site, "server_form": server_form}
    return render(request, "site_surveys/server_checklist.html", context)


@login_required
def mdf_checklist(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        mdf_form = MDFForm(instance=site)

    else:
        # POST data submitted; process data.
        mdf_form = MDFForm(instance=site, data=request.POST)
        if mdf_form.is_valid():
            mdf_form.save()
            context = {"site": site}
            return render(request, "site_surveys/site.html", context)

    # Display a blank or invalid form.
    context = {"site": site, "mdf_form": mdf_form}
    return render(request, "site_surveys/mdf_checklist.html", context)


@login_required
def idf_checklist(request, site_id):
    """Edit an existing site."""
    site = get_object_or_404(Site, id=site_id)

    if request.method != "POST":
        # No data submitted; create a blank form.
        idf_form = IDFForm(instance=site)

    else:
        # POST data submitted; process data.
        idf_form = IDFForm(instance=site, data=request.POST)
        if idf_form.is_valid():
            idf_form.save()
            context = {"site": site}
            return render(request, "site_surveys/site.html", context)

    # Display a blank or invalid form.
    context = {"site": site, "idf_form": idf_form}
    return render(request, "site_surveys/idf_checklist.html", context)


@login_required
def export_all_sites(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export_all_sites.csv"'
    export_sites = Site.objects.all()

    my_writer = writer(response)
    my_writer.writerow([
        "title", "first_name", "last_name", "email", "street_address", "city", "state", "zip_code", "site_type",
        "front", "back", "left", "right", "router_one", "router_two", "switch_one", "switch_two", "server_one",
        "server_two", "mdf", "idf",
    ])

    for export_site in export_sites:
        my_writer.writerow([
            export_site.title,
            export_site.first_name,
            export_site.last_name,
            export_site.email,
            export_site.street_address,
            export_site.city,
            export_site.state,
            export_site.zip_code,
            export_site.site_type,
            export_site.front,
            export_site.back,
            export_site.left,
            export_site.right,
            export_site.router_one,
            export_site.router_two,
            export_site.switch_one,
            export_site.switch_two,
            export_site.server_one,
            export_site.server_two,
            export_site.mdf,
            export_site.idf,
        ])
    return response


@login_required
def export_site(request, site_id):
    export_site = get_object_or_404(Site, id=site_id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="export_site_{export_site.title}.csv"'

    my_writer = writer(response)
    my_writer.writerow([
        "title", "first_name", "last_name", "email", "street_address", "city", "state", "zip_code", "site_type",
        "front", "back", "left", "right", "router_one", "router_two", "switch_one", "switch_two", "server_one",
        "server_two", "mdf", "idf",
    ])
    my_writer.writerow([
        export_site.title,
        export_site.first_name,
        export_site.last_name,
        export_site.email,
        export_site.street_address,
        export_site.city,
        export_site.state,
        export_site.zip_code,
        export_site.site_type,
        export_site.front,
        export_site.back,
        export_site.left,
        export_site.right,
        export_site.router_one,
        export_site.router_two,
        export_site.switch_one,
        export_site.switch_two,
        export_site.server_one,
        export_site.server_two,
        export_site.mdf,
        export_site.idf,
    ])
    return response


@login_required
def useful_links(request):
    return render(request, "site_surveys/useful_links.html")


@login_required
def documentation(request):
    return render(request, "site_surveys/documentation.html")


@login_required
def contacts(request):
    return render(request, "site_surveys/contacts.html")
