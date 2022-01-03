from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    book_url = models.CharField(max_length=150)
    book_image_url = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name="favorite_books")
    category = models.ManyToManyField(Category,related_name="book_category")


# Your first goal should be creating a Book model and showing an index of all books. Some details:

# - Books have, at a minimum, a title, author, description, URL, and date added to the database (`created_at`).
# - Book URLs (the URL field in the database) should be unique.
# - Admins can add, edit, and delete books.
# - You should have initial data for books (a CSV is provided, but you can edit it to fit your data).
# - Books should be displayed in order with the most recently added at the top.
