from django.contrib import admin
from .models import Movie, Network, Language, Quality, Link


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "updated"]
    list_filter = ["title", "updated", "published"]
    search_fields = ["title"]


class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "updated"]
    list_filter = ["name", "updated", "created"]
    search_fields = ["name"]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Network)
admin.site.register(Language)
admin.site.register(Quality)
admin.site.register(Link, LinkAdmin)
