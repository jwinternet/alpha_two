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
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'style': 'width: 300px;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;'}))
    # today_date = forms.DateField(
    #     widget=forms.DateInput(
    #         format='%Y-%m-%d',
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Select a date',
    #             'type': 'date'
    #         }
    #     ),
    # )
    favorite_fruit = forms.MultipleChoiceField(
        label="What is your favorite fruit?",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FRUIT_CHOICES,
    )
    age = forms.IntegerField(
        label="How old are you?",
        widget=forms.Select(choices=INTEGER_CHOICES)
    )

    class Meta:
        model = Site
        fields = ["title", "text", "first_name", "last_name", "email", "age", "favorite_fruit"]
        labels = {
            "title": "Site ID - ",
            "text": "Text - ",
            "first_name": "First Name - ",
            "last_name": "Last Name - ",
            "email": "Email - ",
            "age": "Age - ",
            "favorite_fruit": "Fruit - ",
        }
