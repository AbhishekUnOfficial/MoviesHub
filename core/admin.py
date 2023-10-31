from django.contrib import admin
from .models import Comment, Movie, Network, Language, Quality, Link


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "updated"]
    list_filter = ["title", "updated", "published"]
    search_fields = ["title"]


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "updated"]
    list_filter = ["name", "updated", "created"]
    search_fields = ["name"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    pass
