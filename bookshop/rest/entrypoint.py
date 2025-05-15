from fastapi import FastAPI, status, Depends, Security, HTTPException

from fastapi.security import APIKeyHeader, HTTPBasic, HTTPBasicCredentials

from prometheus_fastapi_instrumentator import Instrumentator
from bookshop.model.inmemory import Book
from bookshop.model import get_model
from random import choices


app = FastAPI(title="Book Shop Rental Service")

Instrumentator().instrument(app).expose(app)

CONFIG = "memory"

API_KEY_NAME = "X-API-Key"
API_KEY_VALUE = "this_should_be_a_better_key"

USERNAME = "husnusensoy"
PASSWORD = "1234567890"

"""

User -> Service (auth,https,...)
 
User -> API Gategway -> Service (no auth, http,..)

"""


"""
  header[API_KEY_NAME] vs header.get(API_KEY_NAME)
"""
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
basicauth = HTTPBasic()


@app.get("/login")
def login():
    "This requires password auth"
    ...


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY_VALUE:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid API Key. Check {API_KEY_NAME} at header",
        )

    return api_key


def get_username(credentials: HTTPBasicCredentials = Depends(basicauth)):
    # is_user_correct = secrets.compare_digest(credentials.username, USERNAME)
    is_user_correct = credentials.username == USERNAME
    is_passw_correct = credentials.password == PASSWORD

    if not (is_user_correct and is_passw_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    return credentials.username


@app.get("/books/", tags=["book"])
def get_books() -> list[Book]:
    db = get_model(CONFIG)

    return db.get_books()


@app.get("/books/{id}", tags=["book"])
def get_a_book(book_id: int, api_key: str = Depends(verify_api_key)) -> Book:
    db = get_model(CONFIG)

    return db.get_book(book_id)


@app.post("/books/", tags=["book"], status_code=status.HTTP_201_CREATED)
def create_book(book: Book, user_name: str = Depends(get_username)):
    print(f"{user_name} is calling create book API")
    db = get_model(CONFIG)

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
