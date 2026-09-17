from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "isbn", "category", "quantity", "available_quantity")
    search_fields = ("title", "author", "isbn", "category")
    list_filter = ("category",)
