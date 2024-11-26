from argparse import ArgumentParser

from app.core.library import Library


def clear_library(args: dict, library: Library):
    confirm_delete = input("Вы уверены, что хотите удалить весь каталог? y/n ")
    if confirm_delete in ["y", "Y", "YES", "yes"]:
        library.clear()
        print("Все книги удалены")
    else:
        print("Удаление отменено")

    library.save()


def create_command(subparsers):
    parser: ArgumentParser = subparsers.add_parser(
        "clear", help="Удалить все книги в каталоге"
    )
    parser.set_defaults(func=clear_library)
