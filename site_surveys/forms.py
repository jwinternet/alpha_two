#!/usr/bin/python3.12
from django import forms

from .models import Site


INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 99)]
FRUIT_CHOICES = [
    ("orange", "Oranges"),
    ("cantaloupe", "Cantaloupes"),
    ("mango", "Mangoes"),
    ("honeydew", "Honeydews"),
]


class SiteForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Site ID', 'style': 'width: 300px;'})
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
    favorite_fruit = forms.MultipleChoiceField(
        label="What is your favorite fruit?",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FRUIT_CHOICES,
    )

    class Meta:
        model = Site
        fields = ["title", "text", "first_name", "last_name", "email", "age", "favorite_fruit"]
