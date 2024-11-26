"""
CLI-приложение для управления электронной библиотекой.\n
Оно предоставляет функциональные возможности для добавления, удаления, поиска и составления списка книг, а также обновления их статуса.

"""

from argparse import ArgumentParser, Namespace

from app.commands import add, clear, delete, find, list, status
from app.core.library import Library

library = Library()


def main():
    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(
        title="Команды",
        dest="command",
        metavar="",
    )

    # Добавить команды
    add.create_command(subparsers)
    delete.create_command(subparsers)
    find.create_command(subparsers)
    list.create_command(subparsers)
    status.create_command(subparsers)
    clear.create_command(subparsers)

    args: Namespace = parser.parse_args()

    if args.command:
        args.func(args.__dict__, library)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
