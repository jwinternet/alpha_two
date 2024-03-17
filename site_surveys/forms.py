#!/usr/bin/python3.12
from django import forms

from .models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ["title", "text"]
        labels = {"title": ""}
