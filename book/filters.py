import django_filters
from book.models  import Book


class BookFilter(django_filters.FilterSet):
    class Meta: 
        model = Book
        fields = {
            'title': ['exact', 'contains'],
            'author': ['exact', 'contains'],
            'genrs': ['exact', 'contains'], # contains imitom rom sheiZleba ramodenime janri uyos da erterts tu mainc ergeba 
        }



           
