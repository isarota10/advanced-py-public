from fastapi.testclient import TestClient


from bookshop.rest.entrypoint import app


client = TestClient(app)


def test_get_books():
    assert len(client.get("/books/").json()) >= 2
