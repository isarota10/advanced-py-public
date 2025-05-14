# Book Shop API

## Data

### Books

* id (int)
* title (string)
* author (name)
* available (bool)

### Users
* id
* name

### Borrow Records

* user_id
* book_id
* borrow_date
* return_date

## Endpoints

### Books

* GET /books
* GET /books/{id}
* POST /books
* PUT /books/{id}
* DELETE /books/{id}

### Users
* GET /users
* POST /users


### Borrowing

* POST /borrow - Body: `{"user_id":1, "book_id": 1}`
  * Mark a book as borrowed
  * Set ` available=False`
  * Add a borrow record
* POST /return - Body: `{"user_id":1, "book_id": 1}`
  * Mark a book as available
  * Update return_date

