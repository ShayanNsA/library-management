from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('', views.home, name='home'),
    path('books/create/', views.book_create, name='book-create'),
    path('authors/add/', views.add_author, name='add_author'),
    path('genres/add/', views.add_category, name='add_category'),

    path('books/detail/<int:book_id>/', views.book_details, name='book-detail'),
    path('books/update/<int:book_id>/', views.update_book, name='book-update' ),

    path('books/delete/<int:book_id>/', views.delete_book, name='book-delete'),

    path('books/bulk_delete/', views.bulk_delete, name='book-bulk-delete'),
]