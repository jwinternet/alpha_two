#!/usr/bin/python3.12
from django import forms

from .models import Site


INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 99)]


class SiteForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        required=True,
        min_length=4,
        max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'Site ID', 'style': 'width: 300px;'}),
    )
    text = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Enter information here.', 'style': 'width: 300px;'})
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
    age = forms.IntegerField(
        label="Age: ",
        widget=forms.Select(choices=INTEGER_CHOICES)
    )
    site_type = forms.CharField(
        label="Site Type: ",
        required=False,
        widget=forms.Select(choices=Site.SITE_TYPES),
    )

    class Meta:
        model = Site
        fields = ["title", "text", "first_name", "last_name", "email", "age", "site_type"]


class AddressForm(forms.ModelForm):
    address = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'style': 'width: 300px;'})
    )

    class Meta:
        model = Site
        fields = ["address"]
