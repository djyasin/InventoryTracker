from django import forms
from .models import Book, Category, User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    name = forms.CharField(max_length=100, help_text="Name")
    email = forms.EmailField(max_length=100, help_text="Email Address")

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "description",
            "book_url",
            "book_image_url",
            "favorited_by",
            "category",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "name",
        ]
