from rest_framework import serializers
from .models import Book


class LevelsField(serializers.Field):

    def to_representation(self, value):
        arr = value.split(',')
        return arr

    def to_internal_value(self, data):
        # here you need to implement your transform logic
        return ','.join(data)


class BookSerializer(serializers.ModelSerializer):
    authors = LevelsField()

    class Meta:
        model = Book
        fields = [
            'id',
            'external_id',
            'title',
            'authors',
            'published_year',
            'acquired',
            'thumbnail'
        ]
