from bookshop.model import get_model
from bookshop.model.exceptions import BookNotFound, BookExists
import pytest
import sys


def test_books():
    db = get_model()

    assert len(db.get_books()) == 2


def test_get_book():
    db = get_model()

    assert db.get_book(1) is not None


def test_get_book_not_found():
    db = get_model()

    with pytest.raises(BookNotFound):
        assert db.get_book(10) is not None


def test_create_book_ok():
    db = get_model()

    db.create_book("Devlet Ana", "Kemal Tahir")

    assert len(db.get_books()) == 3


def test_create_book_nok():
    db = get_model()

    with pytest.raises(BookExists):
        db.create_book("harry potter", "Rowling")


def test_update():
    db = get_model()

    book = db.get_book(0)
    book.author = "J.K. Rowling"

    db.update_book(0, book)


def test_corrup_with_update():
    db = get_model()

    book = db.get_book(0)
    book.title = "Suç ve Ceza"

    db.update_book(0, book)

    print(db.books, file=sys.stderr)

    assert db._find_book_by_title("Suç ve Ceza") is not None
