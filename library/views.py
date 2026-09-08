from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Book
from .forms import BookForm, AuthorForm, CategoryForm
from django.db.models import Q



from django.db.models import Q
from django.shortcuts import render
from .models import Book


def book_list(request):
    books = Book.objects.all()


    search = request.GET.get('search', '')

    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(authors__first_name__icontains=search) |
            Q(authors__last_name__icontains=search)
        ).distinct()


    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 3000000)

    if min_price:
        books = books.filter(price__gte=min_price)

    if max_price:
        books = books.filter(price__lte=max_price)


    start_year = request.GET.get('start_year', 1900)
    end_year = request.GET.get('end_year', 2030)

    if start_year:
        books = books.filter(publish_date__year__gte=start_year)

    if end_year:
        books = books.filter(publish_date__year__lte=end_year)

    return render(
        request,
        'library/book_list.html',
        {
            'books': books,
            'search': search,

            'min_price': min_price,
            'max_price': max_price,

            'start_year': start_year,
            'end_year': end_year,
        }
    )

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

def book_details(request, book_id):
    book= Book.objects.get(pk=book_id)

    return render(request, 'library_book_detail.html', {'book': book})

def update_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':

        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return redirect('book-detail',book_id=book.id)

    else:
        form = BookForm(instance=book)

    return render(request,'library/book_update.html',
                  {'form': form,
                           'book' : book
    })

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('book-list')

    else:
        pass

    return redirect('book-detail',book_id=book.id)

def bulk_delete(request):
    if request.method == 'POST':
        selected_books = request.POST.getlist('selected_books')

        Book.objects.filter(id__in=selected_books).delete()

    return redirect('book-list')


def bulk_delete(request):

    if request.method == 'POST':

        selected_books = request.POST.getlist('selected_books')

        Book.objects.filter(id__in=selected_books).delete()

    return redirect('book-list')