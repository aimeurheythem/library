from django.urls import path
from .views import *

urlpatterns = [
    # all books
    path("books/", getBook, name="book"),
    # book by id
    path("books/<str:pk>", getBookByID, name="book_id"),
    # add book
    path("books/add/", add_book, name="add_book"),
    # update book
    path("books/update/<str:pk>/", update_book, name="update_book"),
    # delete book
    path("books/delete/<str:pk>/", delete_book, name="delete_book"),
    # get students
    path("students/", getStudent, name="student"),
    # add new student
    path("students/add/", add_student, name="add_student"),
    # get archive
    path("archive/", getArchive, name="archive"),
    # get rented books
    path("rentedbooks/", getRentBook, name="rented_books"),
    # create a rent book model
    path("rentbook/", rentBook, name="rent_book"),
]
