from rest_framework import serializers
from django.conf import settings
from .models import Book, Request


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ('owner',)

class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = "__all__"