from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Book
from .serializers import BookSerializer

class BookListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.filter(user=request.user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class BookDetailAPIView(APIView):
    permission_classes = [IsOwner]

    def get_object(self, pk):
        obj = get_object_or_404(Book, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=204)

class BookCopyAPIView(APIView):
    permission_classes = [IsOwner]

    def get_object(self, pk):
        obj = get_object_or_404(Book, pk=pk)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=200)
    
    def post(self, request, pk, format=None, **kwargs):
        book = self.get_object(pk)
        book.pk = None
        serializer = BookSerializer(book, data=book.__dict__)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
