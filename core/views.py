from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Movie


class AllMoviesView(ListView):
    model = Movie
    template_name = "core/all_movies.html"
    context_object_name = "movies"


class SingleMovieView(DetailView):
    model = Movie
    template_name = "core/single_movie.html"
