from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=75, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"


class Book(models.Model):
    title = models.CharField(max_length=150, blank=True)
    author = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=500, blank=True)
    book_url = models.CharField(max_length=150, blank=True)
    book_image_url = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    favorited_by = models.ManyToManyField(
        User, related_name="favorite_books", blank=True
    )
    category = models.ManyToManyField(
        Category, related_name="book_category", blank=True
    )
