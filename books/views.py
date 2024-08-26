from django.shortcuts import render , redirect
from .models import Book
from .forms import ContactForm
from django.contrib import messages

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def about(request):
    return render(request, 'books/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('books:contact_view')
        else:
            form = ContactForm()
    return render(request, 'books/contact.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
