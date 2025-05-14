from locust import HttpUser, task
from random import randint


class HelloBenchmark(HttpUser):
    @task(9)
    def check_books(self):
        self.client.get("/books/")

    @task(1)
    def check_book_with_id(self):
        self.client.get(f"/books/{randint(0, 5)}")
