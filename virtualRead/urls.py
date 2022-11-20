"""virtualRead URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from readingApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.GenreView.as_view(), name="genre"),
    path('book/create', views.CreateBookView.as_view(), name="createBook"),
    path('genre/create', views.CreateGenreView.as_view(), name="createGenre"),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name="detailedGenre"),
    path('book/<str:pk>', views.BookDetailView.as_view(), name="book"),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)