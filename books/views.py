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

def add_book(request):
    if request.method == "GET":
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user
            form.save()
            return redirect(to='home')
    return render(request, "add_book.html", {"form": form}) 

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {"book": book})
