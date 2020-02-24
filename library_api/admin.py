from django.contrib import admin
from .models import Books, Borrower

admin.site.register(Books)
admin.site.register(Borrower)