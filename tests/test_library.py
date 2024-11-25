import unittest

from app.core.book import Book
from app.core.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(filename="test.json")
        self.library.clear()
        self.book = Book("Test book", "Test author", 2000)

    def test_add(self):
        self.library.add(self.book)
        self.assertEqual(self.library.count, 1)

    def test_delete(self):
        self.library.add(self.book)
        self.library.delete(self.book.id)
        self.assertEqual(self.library.count, 0)

    def test_clear(self):
        for _ in range(5):
            book = Book("Test book", "Test author", 2000)
            self.library.add(book)
        self.library.clear()
        self.assertFalse(self.library.count)

    def test_get_book_by_id(self):
        self.library.add(self.book)
        book = self.library.get_book_by_id(self.book.id)
        self.assertEqual(self.book.id, book["id"])

    def test_get_books_by_title(self):
        self.library.add(self.book)
        book = self.library.get_books_by_title(self.book.title)[0]
        self.assertEqual(self.book.title, book["title"])

    def test_get_books_by_author(self):
        self.library.add(self.book)
        book = self.library.get_books_by_author(self.book.author)[0]
        self.assertEqual(self.book.author, book["author"])

    def test_get_books_by_year(self):
        self.library.add(self.book)
        book = self.library.get_books_by_year(self.book.year)[0]
        self.assertEqual(self.book.year, book["year"])

    def test_get_books(self):
        for _ in range(5):
            book = Book("Test book", "Test author", 2000)
            self.library.add(book)
        books = self.library.get_books()
        self.assertEqual(self.library.count, len(books))
