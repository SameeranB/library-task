from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .serializers import *
from .models import Book,Author
# Create your views here.


class BookView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = 'BOOK_ID'
    queryset = Book.objects.all()

    def retrieve(self, request, *args, **kwargs):
        book = Book.objects.get(BOOK_ID__exact=kwargs['BOOK_ID'])
        author = Author.objects.get(AUTHOR_ID__exact=book.AUTHOR.AUTHOR_ID)
        return Response({'BOOK_ID':book.BOOK_ID,'NAME':book.NAME,'AUTHOR_NAME':author.NAME,'AUTHOR_ID':author.AUTHOR_ID})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

class BookCreate(CreateAPIView):
    serializer_class = BookCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response



class AuthorView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    lookup_field = 'AUTHOR_ID'
    queryset = Author.objects.all()

    def retrieve(self, request, *args, **kwargs):
        author = Author.objects.get(AUTHOR_ID__exact=kwargs['AUTHOR_ID'])
        books = Book.objects.filter(AUTHOR__AUTHOR_ID=author.AUTHOR_ID)
        return Response({'AUTHOR_ID':author.AUTHOR_ID, 'NAME':author.NAME, 'BOOKS':books.values()})

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response


class AuthorCreate(CreateAPIView):
    serializer_class = AuthorCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response
