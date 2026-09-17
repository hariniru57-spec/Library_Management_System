from django.urls import path
from .api_views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="api_book_list"),
    path("books/<int:pk>/", BookDetailAPIView.as_view(), name="api_book_detail"),
]
