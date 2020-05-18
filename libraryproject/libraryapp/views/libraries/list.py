import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from libraryapp.models import Library, Book
from ..connection import Connection
from libraryapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def list_libraries(request):
    if request.method == 'GET':
        
        libraries = Library.objects.all()
        library_books = []
        
        for library in libraries:
            library.books = Book.objects.filter(library_id=library.id)
                
        template = 'libraries/list.html'
        
        context = {
            'all_libraries' : libraries
        }
        
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        
    with sqlite3.connect(Connection.db_path) as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO libraryapp_library
        (
            name, address
        )
        VALUES (?, ?)
        """,
        (form_data['name'], form_data['address']))
        
    return redirect(reverse('libraryapp:libraries'))

def create_library(cursor, row):
    _row = sqlite3.Row(cursor, row)

    library = Library()
    library.id = _row["id"]
    library.name = _row["name"]
    library.address = _row["address"]

    # Note: You are adding a blank books list to the library object
    # This list will be populated later (see below)
    library.books = []

    book = Book()
    book.id = _row["book_id"]
    book.title = _row["book_title"]
    book.author = _row["author"]
    book.year_published = _row["year_published"]
    book.publisher = _row["publisher"]
    book.isbn = _row["isbn"]

    # Return a tuple containing the library and the
    # book built from the data in the current row of
    # the data set
    return (library, book,)