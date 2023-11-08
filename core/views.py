from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, ListView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Comment, Movie
from .forms import CommentForm


@login_required
class AllMoviesView(ListView):
    model = Movie
    template_name = "core/all_movies.html"
    context_object_name = "movies"
    ordering = ["-updated"]


@login_required
class SingleMovieView(DetailView):
    model = Movie
    template_name = "core/single_movie.html"
    context_object_name = "movie"
    slug_field = "slug"
    slug_url_kwarg = "slug"


@login_required
class CommentView(DetailView):
    model = Comment
    template_name = "core/comment_view.html"
    context_object_name = "comments"


def search_post(request):
    # Change to GET for search functionality
    searched = request.GET.get("searched", "")

    movies = (
        Movie.objects.filter(
            Q(title__icontains=searched) | Q(description__icontains=searched)
        )
        if searched
        else Movie.objects.none()
    )

    return render(
        request, "core/search_page.html", {
            "searched": searched, "movies": movies}
    )


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect("all-movies")
        else:
            messages.error(request, "Login failed")

    return render(request, "core/login_page.html")


def RegisterPage(request):
    if request.method == "post":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
        else:
            form = UserCreationForm()
        return render(request, "core/register_page.html", {"form": form})


class AddCommentView(FormView):
    template_name = "core/add_comments.html"
    form_class = CommentForm
    success_url = reverse_lazy("all-movies")
