import json
from pathlib import Path

from app.core.book import Book


class Library:
    def __init__(self, filename: str = "library.json") -> None:
        """Cоздает библиотеку из JSON файла если существует, в противном случае создает пустую библиотеку"""

        # Для быстрого удаления и поиска книги по ID создаем такой словарь
        # Ключ – ID книги, а значение – объект книга
        self.books: dict[str, dict] = {}
        self.count = 0
        self.filepath = Path(__file__).parents[2] / f"data/{filename}"

        # Загружать данные в библиотеку
        if self.filepath.exists():
            with open(self.filepath, "r") as file:
                if file.readline():
                    file.seek(0)
                    books = json.load(file)
                    for book in books:
                        self.books[book["id"]] = book
                    self.count = len(self.books)
        else:
            self.filepath.parent.mkdir(exist_ok=True)
            self.filepath.touch()

    def add(self, book: Book):
        self.books.update({str(book.id): book.to_dict()})
        self.count += 1

    def delete(self, id: str):
        del self.books[id]
        self.count -= 1

    def clear(self):
        self.books.clear()
        self.count = 0

    def get_book_by_id(self, id: str) -> Book | None:
        return self.books.get(id)

    def get_book_by_title(self, title: str) -> Book:
        return [book for book in self.books.values() if title in book["title"]]

    def get_book_by_author(self, author: str) -> Book:
        return [book for book in self.books.values() if author in book["author"]]

    def get_book_by_year(self, year: int) -> Book:
        return [book for book in self.books.values() if book["year"] == year]

    def get_books(self, last: int | None = None):
        books = list(self.books.values())
        if last:
            return books[-last:]
        else:
            return books

    def save(self):
        books = self.get_books()
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(books, file, ensure_ascii=False, indent=4)

    def __str__(self) -> str:
        return f"Библиотека: {self.count} книг"


library = Library()
