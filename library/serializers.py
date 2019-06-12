from rest_framework import serializers
from . import models

class AuthorSerializer(serializers.ModelSerializer):
    BOOKS = serializers.DictField(read_only=True)

    class Meta:
        model = models.Author
        fields = ('AUTHOR_ID', 'NAME', 'BOOKS')

class BookSerializer(serializers.ModelSerializer):
    AUTHOR_ID = serializers.IntegerField(read_only=True)
    AUTHOR_NAME = serializers.CharField(max_length=100, read_only=True)
    class Meta:
        model = models.Book
        fields = ('BOOK_ID', 'NAME', 'AUTHOR_NAME', 'AUTHOR_ID')

class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('NAME', 'AUTHOR', 'PUBLISHED_AT')