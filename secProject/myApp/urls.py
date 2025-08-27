from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_list, name='books_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
]
