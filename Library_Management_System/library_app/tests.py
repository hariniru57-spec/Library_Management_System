from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(
            title="Python Basics", author="Test Author", isbn="TEST-001",
            category="Programming", published_year=2025,
            quantity=5, available_quantity=5
        )
        self.assertEqual(str(book), "Python Basics - Test Author")
