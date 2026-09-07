from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('', views.home, name='home'),
    path('books/create/', views.book_create, name='book-create'),
    path('authors/add/', views.add_author, name='add_author'),
    path('genres/add/', views.add_category, name='add_category'),
]