from django.db import models

# Create your models here.
class Author(models.Model):
    AUTHOR_ID = models.AutoField(primary_key=True)
    NAME = models.TextField()

    def __str__(self):
        return  self.NAME

class Book(models.Model):
    BOOK_ID = models.AutoField(primary_key=True)
    NAME = models.TextField()
    PUBLISHED_AT = models.DateTimeField()
    AUTHOR = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.NAME

