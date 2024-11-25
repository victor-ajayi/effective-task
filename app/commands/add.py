from argparse import ArgumentParser

from app.core.book import Book
from app.core.library import Library


def add_book(args: dict, library: Library):
    book = Book(args["title"], args["author"], args["year"])
    library.add(book)
    print(book, "добавлена")

    library.save()


def create_command(subparsers):
    parser: ArgumentParser = subparsers.add_parser(
        "add", help="Добавить книгу в каталог"
    )
    parser.add_argument("--title", type=str, help="Название книги", required=True)
    parser.add_argument("--author", type=str, help="Автор книги", required=True)
    parser.add_argument("--year", type=int, help="Год издания книги", required=True)
    parser.set_defaults(func=add_book)
