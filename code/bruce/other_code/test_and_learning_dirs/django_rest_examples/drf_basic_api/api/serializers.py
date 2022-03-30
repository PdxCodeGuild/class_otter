from rest_framework import serializers

from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # This tuple can be used to set the order of the serializer response.
        # 'id' is from the database. Django adds this attribute.
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'some_random_attribute')