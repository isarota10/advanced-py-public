from pydantic import BaseModel, Field
from datetime import date

from bookshop.model.exceptions import (
    BookNotFound,
    BookWithTitleNotFound,
    BookExists,
    DatabaseCorruption,
    BadRecord,
)


class Sequence:
    def __init__(self):
        self.current = -1

    def __call__(self, *args, **kwds):
        self.current += 1
        return self.current


class Book(BaseModel):
    id: int = Field(default_factory=Sequence(), frozen=True)
    title: str = Field(min_length=1, max_length=20)
    author: str
    available: bool = True


class User(BaseModel):
    id: int = Field(default_factory=Sequence(), frozen=True)
    name: str


class Borrow(BaseModel):
    book_id: int
    user_id: int
    borrow_date: date
    return_date: date


class InMemoryPythonDB:
    books = [
        Book(title="Harry Potter", author="JK Rowling"),
        Book(title="Suç ve Ceza", author="Doslayevski"),
    ]
    users = [User(name="Joe Dalton"), User(name="Jack Dalton")]

    borrow = []

    def __init__(self):
        pass

    def get_books(self) -> list[Book]:
        return self.books

    def get_book(self, id: int) -> Book:
        book = [b for b in self.books if b.id == id]

        if len(book) == 0:
            raise BookNotFound(id)
        elif len(book) > 1:
            raise DatabaseCorruption()

        return book[0]

    def _find_book_by_title(self, title: str) -> Book:
        book = [b for b in self.books if b.title.capitalize() == title.capitalize()]

        if len(book) == 0:
            return None
            # raise BookWithTitleNotFound(title)
        elif len(book) > 1:
            raise DatabaseCorruption("book")

        return book[0]

    def create_book(self, title: str, author: str) -> Book:
        if (_ := self._find_book_by_title(title)) is not None:
            raise BookExists(title)

        self.books.append(Book(title=title, author=author, available=True))

    def update_book(self, book_id: int, book: Book):
        book_asis = self.get_book(book_id)

        if book_id != book_asis.id:
            raise BadRecord(book_id, book.id)

        if (_ := self._find_book_by_title(book.title)) is not None and _.id != book_id:
            raise BookExists(book.title)

        self.books[book_id] = book
