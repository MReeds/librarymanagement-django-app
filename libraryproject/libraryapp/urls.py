from django.urls import include, path
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name='book_form'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('librarians/', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name="librarian"),
    path('libraries/', list_libraries, name="libraries"),
    path('libraries/<int:library_id>/', library_details, name='library'),
    path('library/form', library_form, name='library_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]