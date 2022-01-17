"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import debug_toolbar
from books import views as books_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', books_views.home, name='home'),
    path('add_book/', books_views.add_book, name="add_book"),
    path('book_library/', books_views.book_library, name="book_library"),
    path('book_detail/<int:pk>', books_views.book_detail, name="book_detail"),
    path('delete_book/<int:pk>/', books_views.delete_book, name='delete_book'),
    path('edit_book/<int:pk>/', books_views.edit_book, name="edit_book"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('add_category/', books_views.add_category, name="add_category"),
]
