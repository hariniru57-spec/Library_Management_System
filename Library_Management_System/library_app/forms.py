from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "isbn", "category", "published_year", "quantity", "available_quantity"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Book title"}),
            "author": forms.TextInput(attrs={"placeholder": "Author name"}),
            "isbn": forms.TextInput(attrs={"placeholder": "ISBN"}),
            "category": forms.TextInput(attrs={"placeholder": "Category"}),
            "published_year": forms.NumberInput(attrs={"min": 1000, "max": 2100}),
            "quantity": forms.NumberInput(attrs={"min": 1}),
            "available_quantity": forms.NumberInput(attrs={"min": 0}),
        }

    def clean(self):
        cleaned = super().clean()
        quantity = cleaned.get("quantity")
        available = cleaned.get("available_quantity")
        if quantity is not None and available is not None and available > quantity:
            self.add_error("available_quantity", "Available quantity cannot exceed total quantity.")
        return cleaned
