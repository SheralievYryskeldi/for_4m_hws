from django.shortcuts import render, get_object_or_404, HttpResponse
from . import models, forms

def all_books(request):
    books = models.Book.objects.all()
    return render(request, "books.html", {"books": books})

def get_book_detail(request):
    book = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail", {"book": book})

def add_book(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FilES)
        if form.is_valid():
            form.save()
            return HttpResponse("Book created successfully")
    else:
        form = forms.BookForm()
    return render(request, "add_books.html", {"form": form})


