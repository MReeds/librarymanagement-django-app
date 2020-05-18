import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Librarian
from ..connection import Connection
from libraryapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def list_librarians(request):
    if request.method == 'GET':
        
        librarians = Librarian.objects.all()

        template_name = 'librarians/list.html'

        context = {
            'all_librarians': librarians
        }

        return render(request, template_name, context)