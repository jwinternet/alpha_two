#!/usr/bin/python3.12
from django import forms

from .models import Site


# INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 99)]


class SiteForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        required=True,
        min_length=4,
        max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'Site ID', 'style': 'width: 300px;'}),
    )
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;'})
    )
    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;'})
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;'})
    )
    street_address = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Street Address', 'style': 'width: 300px;'})
    )
    city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'City', 'style': 'width: 300px;'})
    )
    state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'State', 'style': 'width: 300px;'})
    )
    zip_code = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'ZIP Code', 'style': 'width: 300px;'})
    )
    site_type = forms.CharField(
        label="Site Type: ",
        required=False,
        widget=forms.Select(choices=Site.SITE_TYPES),
    )

    class Meta:
        model = Site
        fields = ["title", "first_name", "last_name", "email", "street_address", "city", "state", "zip_code", "site_type"]


# class FileUploadForm(forms.ModelForm):
#     class Meta:
#         model = Site
#         fields = ["file_upload"]


class PhotoForm(forms.ModelForm):
    front = forms.CharField(
        label="Front: ",
        required=False,
        widget=forms.Select(choices=Site.PHOTO_CHOICES),
    )
    back = forms.CharField(
        label="Front: ",
        required=False,
        widget=forms.Select(choices=Site.PHOTO_CHOICES),
    )
    left = forms.CharField(
        label="Front: ",
        required=False,
        widget=forms.Select(choices=Site.PHOTO_CHOICES),
    )
    right = forms.CharField(
        label="Front: ",
        required=False,
        widget=forms.Select(choices=Site.PHOTO_CHOICES),
    )

    class Meta:
        model = Site
        fields = ["front", "back", "left", "right"]
