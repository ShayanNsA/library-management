from django.shortcuts import render
from django.http import JsonResponse
from .models import Book


def book_list(request):
    books = Book.objects.all()

    return render(request, 'library/book_list.html', {
        'books': books
    })

def home(request):
    return render(request, 'library/home.html')