from django.contrib import admin
from .models import Author, Book, Category

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'publish_date','pages', 'id', 'price' )

    @admin.display(description='Authors')
    def get_authors(self, obj):

        return " ".join([author.first_name + " " + author.last_name for author in obj.authors.all()])



