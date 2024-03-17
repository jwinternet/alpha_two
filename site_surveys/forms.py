#!/usr/bin/python3.12
from django import forms

from .models import Site


INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 32)]
FRUIT_CHOICES = [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
]


class SiteForm(forms.ModelForm):
    favorite_fruit = forms.CharField(
        label='What is your favorite fruit?',
        widget=forms.Select(choices=FRUIT_CHOICES)
    )
    today_date = forms.IntegerField(
        label="What is today's date?",
        widget=forms.Select(choices=INTEGER_CHOICES)
    )

    class Meta:
        model = Site
        fields = ["title", "text", "first_name", "last_name", "email", "age", "favorite_fruit", "today_date"]
        labels = {
            "title": "Site ID - ",
            "text": "Text - ",
            "first_name": "First Name - ",
            "last_name": "Last Name - ",
            "email": "Email - ",
            "age": "Age - ",
            "favorite_fruit": "Fruit - ",
            "today_date": "Today - "
        }
