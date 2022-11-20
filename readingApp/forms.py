from dataclasses import fields
from django import forms
from . import models

class AddBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter name"}),
            "summary": forms.TextInput(attrs={"class": "form-control", "placeholder": "What's in the book?"}),
            "genre": forms.Select(attrs={"class": "form-control"}),
            "thumbnail": forms.FileInput(attrs={"class": "form-control"}),
            "pdf_file": forms.FileInput(attrs={"class": "form-control"}),
        }

class AddGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = "__all__"
        widgets = {
            "genre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a genre"}),
        }