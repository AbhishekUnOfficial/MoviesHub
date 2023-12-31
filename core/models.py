from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


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

    class Meta:
        verbose_name_plural = "qualities"

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    updated = models.DateField(auto_now=True, blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="poster")
    slug = AutoSlugField(populate_from="title")
    published = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)
    released = models.IntegerField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    languages = models.ManyToManyField(Language)
    networks = models.ManyToManyField(Network)
    qualities = models.ForeignKey(
        Quality, on_delete=models.CASCADE, blank=True, null=True
    )
    links = models.ManyToManyField(Link)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Movie, related_name="comments", blank=True, null=True, on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=100, blank=True, null=True)
    feedback = models.TextField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.feedback
