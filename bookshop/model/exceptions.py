class BookNotFound(Exception):
    def __init__(self, book_id: int):
        self.book_id = book_id
        super().__init__(f"Book {book_id} not available in shop")


class BookExists(Exception):
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"Book '{title}' already exists in shop")


class BookWithTitleNotFound(Exception):
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"Book '{title}' not available in shop")


class DatabaseCorruption(Exception):
    def __init__(self):
        super().__init__("One or more constraints are violated")


class BadRecord(Exception):
    def __init__(self, expected_id: int, user_data_id: int):
        self.excepted_id = expected_id
        self.user_data_id = user_data_id

        super().__init__(
            f"Excepted id {expected_id} found to be {user_data_id} by user"
        )
