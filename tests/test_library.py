import unittest

from app.core.book import Book
from app.core.library import Library


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(filename="test.json")
        self.library.clear()
        self.book_data = {"title": "Test book", "author": "Test author", "year": 2000}
        self.book = Book("Test book", "Test author", 2000)

    def test_add_book(self):
        self.library.add(self.book)
        self.assertEqual(self.library.count, 1)

    def test_delete_book(self):
        self.library.add(self.book)
        self.library.delete(str(self.book.id))
        self.assertEqual(self.library.count, 0)
