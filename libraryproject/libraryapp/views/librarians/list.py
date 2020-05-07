import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Librarian
from ..connection import Connection
from libraryapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def list_librarians(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                l.id,
                l.library_id,
                l.user_id,
                u.first_name,
                u.last_name,
                u.email
            from libraryapp_librarian l
            join auth_user u on l.user_id = u.id
            """)

            librarians = db_cursor.fetchall()

        template_name = 'librarians/list.html'

        context = {
            'all_librarians': librarians
        }

        return render(request, template_name, context)