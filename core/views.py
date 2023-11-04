from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, ListView
from django.db.models import Q

from .models import Comment, Movie
from .forms import CommentForm


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
        searched = request.POST.get("searched", "")
        if searched:
            movies = Movie.objects.filter(
                Q(title__icontains=searched) | Q(description__icontains=searched)
            )
        else:
            movies = Movie.objects.none()
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


# def comment_form(request, slug):
#     movie = get_object_or_404(Movie, slug=slug)
#     if request.method == "POST":
#         commentform = CommentForm(request.POST)
#         if commentform.is_valid():
#             new_comment = commentform.save(commit=False)
#             new_comment.post = movie
#             new_comment.save()
#         return HttpResponseRedirect(reverse("single-movie", args=[slug]))
#     else:
#         commentform = CommentForm()
#     return render(
#         request,
#         "core/single_movie.html",
#         {"commentform": commentform, "movie": movie},
#     )


class AddCommentView(FormView):
    template_name = "core/add_comments.html"
    form_class = CommentForm
    success_url = reverse_lazy("all-movies")
