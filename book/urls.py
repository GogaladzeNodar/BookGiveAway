from django.urls import path

from .views import book, request


urlpatterns=[
    # book URLs
path('create/', book.BookCreateView.as_view(), name="book-create"),
path('detail/<int:pk>/', book.BookDetailView.as_view(), name="book-detail"),
path('list/', book.BookListView.as_view(), name="book-list"),

# request urls
path('request/create/', request.RequestCreateView.as_view(), name="request-create"),
path('request/list/', request.RequestListView.as_view(), name="request-list"),
path('request/decision/<int:pk>/', request.RequestDecisionView.as_view(), name="request-decision")

]