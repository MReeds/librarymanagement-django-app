import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library
from libraryapp.models import model_factory
from ..connection import Connection


def get_book(book_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Book)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            b.id,
            b.title,
            b.author,
            b.isbn,
            b.year_published,
            b.publisher,
            b.librarian_id,
            b.library_id
        FROM libraryapp_book b
        WHERE b.id = ?
        """, (book_id,))

        return db_cursor.fetchone()

@login_required
def book_details(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)
        template_name = 'books/detail.html'
        return render(request, template_name, {'book': book})

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_book
                SET title = ?,
                    author = ?,
                    ISBN = ?,
                    year_published = ?,
                    publisher = ?,
                    library_id = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['author'],
                    form_data['ISBN'], form_data['year_published'],
                    form_data['publisher'],
                    form_data["library"], book_id,
                ))

            return redirect(reverse('libraryapp:books'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM libraryapp_book
                    WHERE id = ?
                """, (book_id,))

            return redirect(reverse('libraryapp:books'))