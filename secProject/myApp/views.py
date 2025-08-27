from django.shortcuts import render, get_object_or_404
from .models import Book

def home(request):
    """Home page view"""
    return render(request, 'myApp/home.html')

def books_list(request):
    """Books list page view"""
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'myApp/books.html', context)

def book_detail(request, pk):
    """Book detail page view"""
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'myApp/book_detail.html', context)
