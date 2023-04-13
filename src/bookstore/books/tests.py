from django.test import TestCase
from .models import Book

# Create your tests here.


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            name="Harry Potter",
            author_name="J.K. Rowling",
            genre="fantasy",
            book_type="hardcover",
            price= "25.00"
        )

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.name}"
        self.assertEquals(expected_object_name, "Harry Potter")

    def test_author_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.author_name}"
        self.assertEquals(expected_object_name, "J.K. Rowling")

    def test_author_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("author_name").max_length
        self.assertEquals(max_length, 120)

    def test_genre_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.genre}"
        self.assertEquals(expected_object_name, "fantasy")

    def test_type_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.book_type}"
        self.assertEquals(expected_object_name, "hardcover")

    def test_price_content(self):
        book = Book.objects.get(id=1)
        # expected_object_name = f"{book.price}"

        expected_object_name = format(book.price, '.2f')
        self.assertEquals(expected_object_name, '25.00')
