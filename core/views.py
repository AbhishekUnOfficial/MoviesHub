from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Comment, Movie


class AllMoviesView(ListView):
    model = Movie
    template_name = "core/all_movies.html"
    context_object_name = "movies"
    ordering = ["-updated"]


class PostDetailView(DetailView):
    model = Movie
    template_name = "core/movie_detail.html"
    context_object_name = "movie"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class CommentView(DetailView):
    model = Comment
    template_name = "core/comment_view.html"
    context_object_name = "comments"


def search_post(request):
    if request.method == "POST":
        searched = request.POST.get("searched", "")
        movies = (
            Movie.objects.filter(  # type: ignore
                Q(title__icontains=searched) | Q(description__icontains=searched)
            )
            if searched
            else Movie.objects.none()  # type: ignore
        )

        return render(
            request, "core/search_page.html", {"searched": searched, "movies": movies}
        )


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect("all-movies")
        else:
            messages.error(request, "Login failed")
    return render(request, "core/login_page.html")


def register_page(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
    else:
        form = UserCreationForm()
    return render(request, "core/register_page.html", {"form": form})


def comment_form(request):
    if request.method == "POST":
        # name = should be fetch automatically if user logged in
        user_comment = request.POST.get("comment")
        comment = Comment.objects.get("feedback")  # type: ignore
        comment.save()
    template_name = "core/movie_detail.html"
    return render(request, template_name)
