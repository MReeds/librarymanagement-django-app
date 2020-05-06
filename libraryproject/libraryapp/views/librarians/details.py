import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian, model_factory
from ..connection import Connection

def get_librarian(librarian_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT 
            lib.id, 
            lib.library_id, 
            us.first_name, 
            us.last_name, 
            us.username,
            us.email
        FROM libraryapp_librarian lib
        JOIN auth_user us ON lib.id = us.id
        WHERE lib.id = ?
        """, (librarian_id,))
        
        return db_cursor.fetchone()
    
@login_required
def librarian_details(request, librarian_id):
    if request.method == "GET":
        librarian = get_librarian(librarian_id)
        
        template = 'librarians/detail.html'
        context = {
            'librarian': librarian
        }
        
        return render(request, template, context)