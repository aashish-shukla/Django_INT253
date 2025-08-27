from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'publication_date']
    list_filter = ['author', 'publication_date']
    search_fields = ['title', 'author', 'isbn']
    ordering = ['-created_at']

# Register your models here.

