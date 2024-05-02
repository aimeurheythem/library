from rest_framework import serializers
from .models import *


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBook
        fields = "__all__"


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = "__all__"


class LibraryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCard
        fields = "__all__"