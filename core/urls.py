from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AllMoviesView, MovieFormView, SingleMovieView, CommentFormView


urlpatterns = [
    path("", AllMoviesView.as_view(), name="all-movies"),
    path("create/", MovieFormView.as_view(), name="movie-form"),
    path("<slug:slug>/", SingleMovieView.as_view(), name="single-movie"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
