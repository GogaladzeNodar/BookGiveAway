from django.urls import path
from .views import BookCreateView, BookDetailView, BookListView


urlpatterns=[
path('create/', BookCreateView.as_view(), name="book-create"),
path('detail/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
path('list/', BookListView.as_view(), name="book-list"),
]