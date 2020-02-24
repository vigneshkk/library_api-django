from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.home , name="home"),
    path('borrower/',views.BorrowerList.as_view(), name="borrowerlist"),
    path('books/',views.BooksList.as_view(), name="BookList")
]
