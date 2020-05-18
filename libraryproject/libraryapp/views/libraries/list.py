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
        
        template = 'libraries/list.html'
        
        context = {
            'all_libraries' : libraries
        }
        
        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        
        new_library = Library.objects.create(
        name = form_data['name'],
        address = form_data['address']
        )
        
    return redirect(reverse('libraryapp:libraries'))
