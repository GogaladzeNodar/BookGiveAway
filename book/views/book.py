from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from book.filters import BookFilter
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# First of all, "ra aris Sheni gen gegmaa"
# CRUD for Books, 
# createrequest view and Updaterequest view chuqebisTvis   --> es sxva failshi jobia <--


class BookCreateView(APIView):
   
    # request must be POST
    # serialize data and if it is valid save
    #return response
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['owner'] = self.request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookListView(ListAPIView):
    # request GET
    # all book
    #serialize, save, Response
    # def get(self, request):
    #     books = Book.objects.all()
    #     book_filter = BookFilter(request.GET, queryset=books )
    #     filtered_queryset = book_filter.qs
    #     serializer = BookSerializer(filtered_queryset, many=True)
    #     return Response(serializer.data)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
    

class BookDetailView(APIView):
    # here must be 3 request GET - to see the special book, PUT to modifie book, and delete to delete book 
    # danarcheni logika sxva view- ebis msgavsad 
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)