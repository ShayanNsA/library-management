from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('', views.home, name='home'),
    path('books/create/', views.book_create, name='book-create'),
]