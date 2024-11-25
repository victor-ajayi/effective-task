import sys

from app.core.book import BookStatus
from app.core.library import library


def change_status(args: dict):
    book = library.get_book_by_id(args["id"])
    if not book:
        sys.stderr.write("Ошибка: Не существует книга с этим ID")
        sys.exit(1)
    book["status"] = BookStatus(args["status"]).value
    print(book)

    library.save()


def create_command(subparsers):
    parser = subparsers.add_parser(
        "status", help="Изменить статус книги ('В наличии', 'Выдана')"
    )
    parser.add_argument("status", type=str, help="Новый статус книги")
    parser.add_argument("--id", type=str, help="ID книги", required=True)
    parser.set_defaults(func=change_status)
