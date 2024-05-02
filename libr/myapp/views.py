from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


# create new book
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
    book = Book.objects.filter(user=request.user).order_by("id")
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
    book.statu = request.data["statu"]

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
        {"details": "Delete Book Successfully!!"}, status=status.HTTP_200_OK
    )


# create new student
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_student(request):
    data = request.data
    serializer = StudentSerializer(data=data)

    if serializer.is_valid():
        new_student = Student.objects.create(**data, user=request.user)
        result = StudentSerializer(new_student, many=False)
        return Response({"New_Student": result.data})
    else:
        return Response(serializer.errors)


# get students from data base
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStudent(request):
    student = Student.objects.filter(user=request.user).order_by("id")
    serializer_student = StudentSerializer(student, many=True)
    return Response({"Students": serializer_student.data})


# updating student data
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if student.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this student!"},
            status=status.Http_403_FORBIDEN,
        )

    student.first_name = request.data["first_name"]
    student.last_name = request.data["last_name"]
    student.birth_date = request.data["birth_date"]
    student.birth_place = request.data["birth_place"]
    student.class_name = request.data["class_name"]

    student.save()
    serializer = StudentSerializer(student, many=False)
    return Response({"student": serializer.data})


# delete student
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if student.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this student!"},
            status=status.Http_403_FORBIDEN,
        )

    student.delete()
    return Response(
        {"details": "Delete Student Successfully!!"}, status=status.HTTP_200_OK
    )


# create new archive model
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_archive(request):
    data = request.data
    serializer = ArchiveSerializer(data=data)

    if serializer.is_valid():
        new = Archive.objects.create(**data, user=request.user)
        result = ArchiveSerializer(new, many=False)
        return Response({"Archive": result.data})
    else:
        return Response(serializer.errors)


# get archive from database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getArchive(request):
    archive = Archive.objects.filter(user=request.user).order_by("id")
    serilizer_archive = ArchiveSerializer(archive, many=True)
    return Response({"Archive": serilizer_archive.data})


# updating archive data
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_archive(request, pk):
    archive = get_object_or_404(Archive, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if archive.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this archive model!"},
            status=status.Http_403_FORBIDEN,
        )

    archive.first_name = request.data["first_name"]
    archive.last_name = request.data["last_name"]
    archive.birth_date = request.data["birth_date"]
    archive.birth_place = request.data["birth_place"]
    archive.class_name = request.data["class_name"]
    archive.document_name = request.data["document_name"]

    archive.save()
    serializer = ArchiveSerializer(archive, many=False)
    return Response({"Archive": serializer.data})


# delete archive model
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_archive(request, pk):
    archive = get_object_or_404(Archive, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if archive.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this archive model!"},
            status=status.Http_403_FORBIDEN,
        )

    archive.delete()
    return Response(
        {"details": "Delete Archive model Successfully!!"}, status=status.HTTP_200_OK
    )


# create new rented book model
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def rentBook(request):
    data = request.data
    serializer = RentSerializer(data=data)

    if serializer.is_valid():
        book = get_object_or_404(Book, id=data.pop("book_id"))
        student = get_object_or_404(Student, id=data.pop("student_id"))

        rentBook = RentBook.objects.create(
            **data, book_id=book, student_id=student, user=request.user
        )
        result = RentSerializer(rentBook, many=False)
        return Response({"Rent Book": result.data})
    else:
        return Response(serializer.errors)


# et rented books from database
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getRentBook(request):
    rent_book = RentBook.objects.filter(user=request.user).order_by("id")
    serializer_rent = RentSerializer(rent_book, many=True)
    return Response({"Rented": serializer_rent.data})


# updating rented books data
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_rentedBooks(request, pk):
    rent = get_object_or_404(RentBook, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if rent.user != request.user:
        return Response(
            {"Error": "Sorry, you can't update this rented model!"},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    # rent.book_id = request.data["book_id"]
    # rent.student_id = request.data["student_id"]
    rent.rent_date = request.data["rent_date"]
    rent.return_date = request.data["return_date"]
    rent.isRented = request.data["isRented"]

    rent.save()
    serializer = RentSerializer(rent, many=False)
    return Response({"rented book updates": serializer.data})


# delete rented books model
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_rentedBook(request, pk):
    rent = get_object_or_404(RentBook, id=pk)

    # in case the user want make update, is not the user who is authentificated now.
    if rent.user != request.user:
        return Response(
            {"Error": "Sorry, you can't delete this rented book!"},
            status=status.Http_403_FORBIDEN,
        )

    rent.delete()
    return Response(
        {"details": "Delete rented book Successfully!!"}, status=status.HTTP_200_OK
    )


# create new rented book model
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def libraryCard(request):
    data = request.data
    serializer = LibraryCardSerializer(data=data)

    if serializer.is_valid():
        student = get_object_or_404(Student, id=data.pop("student_id"))

        libraryCard = LibraryCard.objects.create(
            **data, student_id=student, user=request.user
        )
        result = LibraryCardSerializer(libraryCard, many=False)
        return Response({"Library Card": result.data})
    else:
        return Response(serializer.errors)


# get all library cards
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getLibraryCard(request):
    libraryCard = LibraryCard.objects.filter(user=request.user)
    serializer_card = LibraryCardSerializer(libraryCard, many=True)
    return Response({"Library Cards": serializer_card.data})

# get all library cards
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateLibraryCard(request, pk):
    library_card = get_object_or_404(LibraryCard, id=pk)
    
    if library_card.user != request.user:
        return Response(
            {"Error: You can't make an update uperation for this library card"},
            status=status.HTTP_401_UNAUTHORIZED
        )
        
    library_card.collegeYear = request.data['collegeYear']
    library_card.isValid = request.data['isValid']
    
    library_card.save()
    serializer = LibraryCardSerializer(library_card, many=False)
    return Response({'Library Card Updated': serializer.data})    

# delete library cards
@api_view(["delete"])
@permission_classes([IsAuthenticated])
def deleteLibraryCard(request, pk):
    card = get_object_or_404(LibraryCard, id=pk)
    
    if card.user != request.user:
        return Response(
            {"Error": "Sorry you can't make a delete operation, you are not authentificated"},
            status=status.HTTP_403_FORBIDDEN
        )
    card.delete()
    return Response(
        {"Details": "A Library Card has been deleted succesfully"},
        status=status.HTTP_200_OK
    )
    
# delete all library cards
@api_view(["delete"])
@permission_classes([IsAuthenticated])
def deleteAllLibraryCard(request):
    try:
        LibraryCard.objects.all().delete()
        return Response(
            {"Response": "All library Cards have been deleted"},
            status=status.HTTP_200_OK
            )
    except Exception as e:
        return Response({"Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
