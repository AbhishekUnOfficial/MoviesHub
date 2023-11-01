from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    AllMoviesView,
    SingleMovieView,
    SearchPost,
    LoginPage,
    RegisterPage,
)

urlpatterns = [
    path("", AllMoviesView.as_view(), name="all-movies"),
    path("search/", SearchPost, name="search-movie"),
    path("login/", LoginPage, name="login-page"),
    path("register/", RegisterPage, name="register-page"),
    path("<slug:slug>", SingleMovieView.as_view(), name="single-movie"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
