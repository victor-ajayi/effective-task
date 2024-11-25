import unittest

from app.core.book import Book, BookStatus


class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.book = Book("Book", "Author", 2000)

    def test_change_status(self):
        self.book.change_status(BookStatus.ISSUED)
        self.assertEqual(self.book.status, BookStatus.ISSUED)
