from django.db import models
from autoslug import AutoSlugField


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="poster")
    slug = AutoSlugField(populate_from="title")

    def __str__(self):
        return self.title
