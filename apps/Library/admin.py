from django.contrib import admin

from .models import Author

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'birth_date', 'status')


admin.site.register(Author, AuthorAdmin)