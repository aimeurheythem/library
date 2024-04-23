from django.db import models

# Create your models here.


class StatusChoice(models.TextChoices):
    RENTED = "rented"
    AVAILABLE = "available"
    LOST = "lost"


class RentChoice(models.TextChoices):
    RETRIEVER = "retriever"
    NOTRETRIEVER = "notretriever"


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, default=0
    )
    category = models.CharField(max_length=100)
    class_number = models.CharField(max_length=100, blank=True, null=True)
    entry_date = models.DateField(auto_now=False, blank=True, null=True)
    published_date = models.DateField(auto_now=False, blank=True, null=True)
    statu = models.CharField(
        max_length=200, choices=StatusChoice.choices, null=False, blank=False
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    birth_date = models.DateField(auto_now=False)
    birth_place = models.CharField(max_length=200, blank=False, null=False)
    class_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.first_name


class RentBook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now=False)
    return_date = models.DateField(auto_now=False)
    rent_statu = models.CharField(
        max_length=200, choices=RentChoice.choices, null=False, blank=False
    )


class Archive(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    birth_date = models.DateField(auto_now=False)
    birth_place = models.CharField(max_length=200, blank=False, null=False)
    class_name = models.CharField(max_length=200, blank=False, null=False)
    document_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.first_name
