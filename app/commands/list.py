import json

from app.core.library import library


def list_books(args: dict):
    books = library.get_books(args["last"])
    if books:
        print(json.dumps(books, ensure_ascii=False, indent=4))
    else:
        print("Нет книг в библиотеке.")

    library.save()


def create_command(subparsers):
    parser = subparsers.add_parser("list", help="Отобразить список книг в каталоге")
    parser.add_argument(
        "--last", type=int, help="Количество книг для печати, начиная с конца списка"
    )
    parser.set_defaults(func=list_books)
