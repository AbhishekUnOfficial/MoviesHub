from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="poster")
    slug = models.SlugField(unique=True)
