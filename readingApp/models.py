from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse("genre")

class Book(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    summary = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    thumbnail = models.ImageField(upload_to="images")
    pdf_file = models.FileField(upload_to="pdf")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre")