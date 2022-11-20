from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import models
from . import forms

# Create your views here.
class GenreView(ListView):
    context_object_name = "genres"
    template_name = "readingApp/genre.html"
    model = models.Genre

class BookDetailView(DetailView):
    context_object_name = "book"
    template_name = "readingApp/book.html"
    model = models.Book

class CreateBookView(CreateView):
    template_name = "readingApp/addBook.html"
    model = models.Book
    form_class = forms.AddBookForm

class CreateGenreView(CreateView):
    template_name = "readingApp/addGenre.html"
    model = models.Genre
    form_class = forms.AddGenreForm

class GenreDetailView(DetailView):
    context_object_name = "genre"
    template_name = "readingApp/genreDetailed.html"
    model = models.Genre