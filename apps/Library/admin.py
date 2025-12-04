from django.contrib import admin

from .models import Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_date', 'status')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'pages', 'isbn', 'status')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)