from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='books', null=True)
    authors = models.ManyToManyField("Author", related_name="books")

class Author(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Category(models.Model):

    title = models.CharField(max_length=50)
