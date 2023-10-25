from django.urls import path
from .views import AllMoviesView, SingleMovieView


urlpatterns = [
    path("", AllMoviesView.as_view(), name="all-movies"),
    path("<slug:slug>/", SingleMovieView.as_view(), name="single-movie"),
]
