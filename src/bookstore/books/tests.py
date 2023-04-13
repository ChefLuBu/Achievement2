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
            price="25.00",
        )

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.name}"
        self.assertEquals(expected_object_name, "Harry Potter")

    def test_author_content(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field("author_name").verbose_name
        self.assertEquals(field_label, "J.K. Rowling")

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
        expected_object_name = f"{book.price}"
        self.assertEquals(expected_object_name, "25.00")

    def test_book_list_view(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get("/books/1/")
        no_response = self.client.get("/books/10000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_detail.html")

    def test_book_create_view(self):
        response = self.client.post(
            "/books/new/",
            {"title": "New title", "author": "New author", "price": "10.00"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New title")
        self.assertContains(response, "New author")
        self.assertContains(response, "10.00")

    def test_book_update_view(self):
        response = self.client.post(
            "/books/1/update/",
            {"title": "Updated title", "author": "Updated author", "price": "15.00"},
        )
        self.assertEqual(response.status_code, 302)

    def test_book_delete_view(self):
        response = self.client.post("/books/1/delete/")
        self.assertEqual(response.status_code, 302)
