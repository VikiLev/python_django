from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})

def single_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        return render(request, 'single_book.html', {'book':book})
    except Book.DoesNotExist:
        raise Http404()

