from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title',
            'publish_date',
            'pages',
            'price',
            'category',
            'authors',
        ]