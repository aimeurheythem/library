from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


# create new_book
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_book(request):
    data = request.data
    serializer = BookSerializer(data=data)

    if serializer.is_valid():
        new_book = Book.objects.create(**data, user=request.user)
        result = BookSerializer(new_book, many=False)
        return Response({"New_Book": result.data})
    else:
        return Response(serializer.errors)


# get all books from the database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBook(request):
    book = Book.objects.all().order_by("id")
    serializer_book = BookSerializer(book, many=True)
    return Response({"Books": serializer_book.data})


# get book by id
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getBookByID(request, pk):
    book = get_object_or_404(Book, id=pk)
    serialzer = BookSerializer(book, many=False)
    return Response({"Book": serialzer.data})


# updating book data
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if book.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this book!"},
            status=status.Http_403_FORBIDEN,
        )

    book.title = request.data["title"]
    book.author = request.data["author"]
    book.price = request.data["price"]
    book.category = request.data["category"]
    book.class_number = request.data["class_number"]
    book.entry_date = request.data["entry_date"]
    book.published_date = request.data["published_date"]

    book.save()
    serializer = BookSerializer(book, many=False)
    return Response({"book": serializer.data})


# delete book
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if book.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this book!"},
            status=status.Http_403_FORBIDEN,
        )

    book.delete()
    return Response(
        {"details": "Delete Done Successfully!!"}, status=status.HTTP_200_OK
    )


# create new student
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)

    if serializer.is_valid():
        new_student = Student.objects.create(**data, user=request.user)
        result = BookSerializer(new_student, many=False)
        return Response({"New_Student": result.data})
    else:
        return Response(serializer.errors)


# get students from data base
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStudent(request):
    student = Student.objects.all().order_by("id")
    serializer_student = StudentSerializer(student, many=True)
    return Response({"Students": serializer_student.data})


# create new archive model
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_archive(request):
    data = request.data
    serializer = ArchiveSerializer(data=data)

    if serializer.is_valid():
        new_book = Archive.objects.create(**data, user=request.user)
        result = ArchiveSerializer(new_book, many=False)
        return Response({"New_Archive": result.data})
    else:
        return Response(serializer.errors)


# get archive from database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getArchive(request):
    archive = Archive.objects.all().order_by("id")
    serilizer_archive = ArchiveSerializer(archive, many=True)
    return Response({"Archive": serilizer_archive.data})


# create new rented book model
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rentBook(request):
    data = request.data
    serializer = RentSerializer(data=data)

    if serializer.is_valid():
        rentBook = RentBook.objects.create(**data, user=request.user)
        result = RentSerializer(rentBook, many=False)
        return Response({"Rente Book": result.data})
    else:
        return Response(serializer.errors)


# et rented books from database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getRentBook(request):
    rent_book = RentBook.objects.all().order_by("id")
    serializer_rent = RentSerializer(rent_book, many=True)
    return Response({"Rented": serializer_rent.data})
