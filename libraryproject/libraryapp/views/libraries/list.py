import sqlite3
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from libraryapp.models import Library
from ..connection import Connection
from libraryapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def list_libraries(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Library)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT
                lib.id,
                lib.name,
                lib.address
            FROM libraryapp_library lib
            """)
            
            all_libraries = db_cursor.fetchall()
            
            # for row in dataset:
            #     lib = Library()
            #     lib.id = row["id"]
            #     lib.name = row["name"]
            #     lib.address = row["address"]
                
            #     all_libraries.append(lib)
                
        template_name = 'libraries/list.html'
        
        context = {
            'all_libraries' : all_libraries
        }
        
        return render(request, template_name, context)

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
