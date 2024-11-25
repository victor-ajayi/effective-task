import sys

from app.core.library import library


def delete_book(args: dict):
    confirm_delete = input(f"Вы уверены, что хотите удалить книгу с ID {args.id}? y/n ")
    if confirm_delete in ["y", "Y", "YES", "yes"]:
        try:
            library.delete(args.id)
        except KeyError:
            sys.stderr.write("Ошибка: Не существует книга с этим ID\n")
            sys.exit(1)
        print(f"Книга {args['id']} удалена")
    else:
        print("Удаление отменено")

    library.save()


def create_command(subparsers):
    parser = subparsers.add_parser("delete", help="Удалить книгу из каталога")
    parser.add_argument("--id", help="ID книги", required=True)
    parser.set_defaults(func=delete_book)
