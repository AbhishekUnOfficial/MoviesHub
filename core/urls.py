from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.AllMoviesView.as_view(), name="all-movies"),
    path("search/", views.search_post, name="search-movie"),
    path("login/", views.login_page, name="login-page"),
    path("register/", views.register_page, name="register-page"),
    path("<slug:slug>", views.PostDetailView.as_view(), name="movie-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
