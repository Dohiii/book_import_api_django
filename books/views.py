import requests
import json

from .filters import BooksFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response


class ImportBooks(APIView):
    def put(self, request):
        url = 'https://www.googleapis.com/books/v1/volumes?q=inauthor'
        imported = 0
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        author = body['author']
        api_url = f"{url}:{str(author)}"
        res = requests.get(api_url, timeout=1)
        json_data = json.loads(res.text)
        books_data = json_data['items']

        for i, book in enumerate(books_data):
            imported += 1
            authors = books_data[i]["volumeInfo"]["authors"]
            title = book["volumeInfo"]["title"]
            external_id = book["id"]
            thumbnail = book["volumeInfo"]["previewLink"]
            published_year = book["volumeInfo"]["publishedDate"][0:4]

            print(list(authors))

            payload = {
                'authors': authors,
                'title': title,
                'external_id': external_id,
                'thumbnail': thumbnail,
                'published_year': published_year
            }

            serializer = BookSerializer(data=payload)
            if serializer.is_valid():
                serializer.save()
                continue
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({"imported": imported})


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BooksFilter

