import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Librarian
from ..connection import Connection
from libraryapp.models import model_factory
from django.contrib.auth.decorators import login_required

@login_required
def list_librarians(request):
    if request.method == 'GET':
        
        all_librarians = Librarian.objects.values("id", "user__first_name", "user__last_name")        

        template_name = 'librarians/list.html'

        context = {
            'all_librarians': all_librarians
        }

        return render(request, template_name, context)