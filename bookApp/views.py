from django.shortcuts import render
from .models import Author, Book
from .forms import MyForm


# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_search(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            book_title_value = form.cleaned_data['book_name']
            books = Book.objects.filter(title__icontains=book_title_value)
            return render(request, 'search_book.html', {'books': books, 'form': form})
    else:
        form = MyForm()
    return render(request, 'search_book.html', {'form': form})


