from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Book
from .forms import BookForm, AuthorForm, CategoryForm




def book_list(request):
    books = Book.objects.all()

    return render(request, 'library/book_list.html', {'books': books})

def home(request):
    return render(request, 'library/home.html')


def book_create(request):

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('book-list')

    else:
        form = BookForm()

    return render(request, 'library/book_create.html', {
        'form': form
    })



def add_author(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book-create')

    else:
        form = AuthorForm()

    return render(request, 'library/add_author.html', {'form': form})

def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book-create')

    else:
        form = CategoryForm()

    return render(request, 'library/add_category.html', {'form': form})