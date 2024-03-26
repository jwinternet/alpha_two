#!/usr/bin/python3.12
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager


class Site(models.Model):
    """A specific site location."""

    title = models.CharField(
        max_length=4,
    )
    slug = models.SlugField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField(null=True)
    SITE_TYPES = [
        ("Wawa", "Wawa"),
        ("Sheetz", "Sheetz"),
        ("Thorntons", "Thorntons"),
        ("AT&T", "AT&T"),
        ("Verizon", "Verizon")
    ]
    site_type = models.CharField(
        choices=SITE_TYPES,
        max_length=100
    )
    file_upload = models.FileField(
        upload_to='site_surveys/media/%Y/%m/%d/',
        blank=True
    )
    tags = TaggableManager()

    class Meta:
        ordering = ['-title']

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def get_absolute_url(self):
        return reverse(
            "site_surveys:site",
            args=[self.id]
        )
