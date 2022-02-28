from django.contrib import admin
from .models import Book, Category, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Book)
admin.site.register(User, UserAdmin)
admin.site.register(Category)
