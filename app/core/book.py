import enum
from uuid import uuid4


class BookStatus(enum.Enum):
    AVAILABLE = "В наличии"
    ISSUED = "Выдана"


class Book:
    def __init__(
        self,
        title: str,
        author: str,
        year: int,
        status: BookStatus = BookStatus.AVAILABLE,
    ) -> None:
        self.id = uuid4()
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def change_status(self, status: BookStatus):
        self.status = status

    def to_dict(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status.value,
        }

    def __str__(self) -> str:
        return f"Книга {str(self.id)[:8]}: {self.author}, {self.title}, {self.year}"
