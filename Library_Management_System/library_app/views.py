from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, "library_app/home.html", {"books": books[:6], "total_books": books.count()})

def book_list(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()
    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(isbn__icontains=query) |
            Q(category__icontains=query)
        )
    return render(request, "library_app/books.html", {"books": books, "query": query})

def add_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Book added successfully.")
        return redirect("book_list")
    return render(request, "library_app/book_form.html", {"form": form, "title": "Add Book"})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, "Book updated successfully.")
        return redirect("book_list")
    return render(request, "library_app/book_form.html", {"form": form, "title": "Edit Book"})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect("book_list")
    return render(request, "library_app/confirm_delete.html", {"book": book})
