from django.db import models
from autoslug import AutoSlugField


class Network(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Quality(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    feedback = models.TextField(max_length=200, blank=True, null=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="poster")
    slug = AutoSlugField(populate_from="title")
    published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    released = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    languages = models.ManyToManyField(Language)
    networks = models.ManyToManyField(Network)
    qualities = models.ForeignKey(
        Quality, on_delete=models.CASCADE, blank=True, null=True
    )
    links = models.ManyToManyField(Link)
    comments = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="comments",
    )

    def __str__(self):
        return self.title
