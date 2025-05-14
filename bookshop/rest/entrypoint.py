from fastapi import FastAPI, status
from bookshop.model.inmemory import Book
from bookshop.model import get_model


app = FastAPI(title="Book Shop Rental Service")


@app.get("/books/", tags=["book"])
def get_books() -> list[Book]:
    db = get_model()

    return db.get_books()


@app.get("/books/{id}", tags=["book"])
def get_a_book(book_id: int) -> Book:
    db = get_model()

    return db.get_book(book_id)


@app.post("/books/", tags=["book"], status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    db = get_model()

    return db.create_book(book.title, book.author)


@app.put("/books/{book_id}", tags=["book"], status_code=status.HTTP_201_CREATED)
def update_book(book_id: int, book: Book):
    db = get_model()

    return db.update_book(book_id, book)


@app.delete("/books/{book_id}", tags=["book"], status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    db = get_model()

    return db.delete_book(book_id)


@app.get("/users/", tags=["user"])
def get_users(): ...


@app.post("/users/", tags=["user"])
def create_user(): ...
