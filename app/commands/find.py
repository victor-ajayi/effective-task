from app.core.library import library


def find_book(args: dict):
    if args["title"]:
        books = library.get_book_by_title(args["title"])
        print(books)
    elif args["author"]:
        books = library.get_book_by_author(args["author"])
        print(books)
    elif args["year"]:
        books = library.get_book_by_year(args["year"])
        print(books)

    library.save()


def create_command(subparsers):
    parser = subparsers.add_parser(
        "find", help="Найти книгу по названию или другим параметрам"
    )
    parameter = parser.add_mutually_exclusive_group(required=True)
    parameter.add_argument("--title", type=str, help="Название книги")
    parameter.add_argument("--author", type=str, help="Автор книги")
    parameter.add_argument("--year", type=int, help="Год издания книги")
    parser.set_defaults(func=find_book)
