from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.db.models import Q
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


class CommentView(DetailView):
    model = Comment
    template_name = "core/comment_view.html"
    context_object_name = "comments"


def SearchPost(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        movies = Movie.objects.filter(title__contains=searched)
        return render(
            request, "core/search_page.html", {"searched": searched, "movies": movies}
        )
    else:
        return render(request, "core/search_page.html", {})


def LoginPage(request):
    if request.method == "post":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)

    return render(request, "core/login_page.html")


def RegisterPage(request):
    return render(request, "core/register_page.html")
