from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Book, urlShortener
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from threading import Timer
import random

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
    # 상세 or 리스트에서 바로 복제를 누르는 경우만 있으니, get 요청 불필요
    def post(self, request, pk, format=None):
        book = self.get_object(pk)
        Book.objects.create(category=book.category, amount_moved=book.amount_moved, memo=book.memo, user=book.user)
        return Response(status=201)

def timer_delete(pk):
    data = urlShortener.objects.get(pk=pk)
    data.delete()

@api_view(['POST'])
def makeurl(request, pk):
    obj = get_object_or_404(Book, pk=pk)
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
    shorturl = ("".join(random.sample(s, 6)))
    while urlShortener.objects.filter(shorturl=shorturl):
        shorturl = ("".join(random.sample(s, 6)))
    temp = urlShortener.objects.create(
        origin=obj,
        shorturl=shorturl
    )
    shorturl = "http://localhost:8000/api/books/" + shorturl + "/"
    S = Timer(28800, timer_delete,[temp.pk]).start() # 8시간 뒤 실행
    return Response({"shorturl": shorturl}, status=201)

@api_view(['GET'])
def redirectUrl(request, shorturl):
    try:
        obj = urlShortener.objects.get(shorturl=shorturl)
    except urlShortener.DoesNotExist:
        obj = None
    if obj:
        serializer = BookSerializer(obj.origin)
        return Response(serializer.data, status=200)
    return Response({'삭제된 데이터 입니다.'}, status=400)
