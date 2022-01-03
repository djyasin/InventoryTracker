from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, User
from django.contrib.auth.forms import UserCreationForm
from .forms import BookForm, CategoryForm, UserForm
# Create your views here.
def home(request):
    user = request.user
    books = Book.objects.filter()

    return render(request, "home.html", {"books": books,})

def book_library(request):
    user = request.user
    books = Book.objects.filter()

    return render(request, "book_library.html", {"books": books,})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {"book": book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='/')
    return render(request, "delete_book.html",
                {"book": book})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='/')

    return render(request, "edit_book.html", {
        "form": form, "book": book, "pk": pk})

def add_book(request):
    if request.method == "POST":
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            return redirect("book_detail", pk=book.pk)
    else:
        form = BookForm()

    return render(request, "add_book.html", {"form": form})