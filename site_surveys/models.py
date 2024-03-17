#!/usr/bin/python3.12
from django.db import models
from django.contrib.auth.models import User


class Site(models.Model):
    """A specific site location."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
