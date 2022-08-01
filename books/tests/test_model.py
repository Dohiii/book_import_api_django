from django.test import TestCase
from books import models

class BookTest(TestCase):
    """Test module for BookModel"""

    def test_create_book(self):
        """Test creating book is successfull"""
        book = models.Book.objects.create(
            title='Sample Title',
            authors=["Mark Twain"],
            published_year='2022',
            acquired=True
        )

        self.assertEqual(str(book), book.title)
