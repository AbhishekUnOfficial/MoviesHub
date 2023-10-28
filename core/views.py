from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, detail

from core.forms import CommentForm
from .models import Comment, Movie


class AllMoviesView(ListView):
    model = Movie
    template_name = "core/all_movies.html"
    context_object_name = "movies"
    ordering = ["-updated"]


class SingleMovieView(DetailView):
    model = Movie
    template_name = "core/single_movie.html"
    context_object_name = "movie"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class CommentFormView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "core/comment_form.html"
    success_url = reverse_lazy("detail-view")
    context_object_name = "comments"


class CommentView(DetailView):
    model = Comment
    template_name = "core/comment_view.html"
    context_object_name = "comments"
