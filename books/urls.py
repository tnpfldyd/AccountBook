from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookListAPIView.as_view()), # 가계부 리스트 및 생성
    path('<int:pk>/', views.BookDetailAPIView.as_view()), # 가계부 디테일 및 수정 및 삭제
    path('<int:pk>/copy/', views.BookCopyAPIView.as_view()), #가계부 디테일 및 복제
]