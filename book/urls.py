from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.all_books, name="books_all_url"),
    path('add-books/', views.add_book, name="add_book")
]