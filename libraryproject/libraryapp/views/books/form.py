import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from .details import get_book
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


def get_libraries():
    return Library.objects.all()

@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/forms.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)
    
@login_required
def book_edit_form(request, book_id):

    if request.method == 'GET':
        book = get_book(book_id)
        libraries = get_libraries()

        template = 'books/forms.html'
        context = {
            'book': book,
            'all_libraries': libraries
        }

        return render(request, template, context)