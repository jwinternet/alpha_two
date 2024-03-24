#!/usr/bin/python3.12
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Site(models.Model):
    """A specific site location."""

    title = models.CharField(
        max_length=4,
        # help_text="The 4-digit ID of the specific location.",
        # verbose_name="ISBN number of the book."
    )
    slug = models.SlugField(max_length=250)
    date_added = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    favorite_fruit = models.CharField(max_length=100)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def get_absolute_url(self):
        return reverse(
            "site_surveys:site",
            args=[self.id]
        )
