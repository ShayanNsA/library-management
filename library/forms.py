from django import forms
from .models import Book, Author, Category


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

        widgets = {'publish_date': forms.DateInput(attrs={'type': 'date'}), }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('قیمت باید مثبت باشه')
        return price


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = [
            'first_name',
            'last_name',
        ]


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = [
            'title',
        ]