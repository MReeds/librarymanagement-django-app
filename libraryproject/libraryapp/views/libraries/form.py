import sqlite3
from libraryapp.models import model_factory
from ..connection import Connection
from django.shortcuts import render
from libraryapp.models import Library
from django.contrib.auth.decorators import login_required

def get_libraries():
    return Library.objects.all()

@login_required
def library_form(request):
    if request.method == "GET":
        libraries = get_libraries()
        template = 'libraries/form.html'
        context = {
            'all_libraries': libraries
        }
    
        return render(request, template, context)