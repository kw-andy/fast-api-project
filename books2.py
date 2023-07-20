from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is ')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, mx_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1000, lt=2033)

    class Config:
        schema_extra = {
            'example': {
                'title': 'a new book',
                'author': 'codingwithandy',
                'description': 'a new book',
                'rating': '5',
                'published_date': 1993
            }
        }


BOOKS = [
    Book(1, "Fast API Udemy", "Robby", "A very nice book", 5, 2002),
    Book(2, "L'idiot", "Doestoievski", "Un grand livre", 5, 1890),
    Book(3, "Prison notebooks", "Gramsci", "La réflexion du 20ème siècle", 5, 1932),
    Book(4, "Dune", "Herbert", "Splendide", 5, 1968),
    Book(5, "Sur la route", "Kerouac", "La liberté !", 5, 1955),
    Book(6, "La route", "McFarrell", "Horrible pourtant poètique", 5, 1968),
    ]


@app.get("/allthebooks/")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.get("/books/{book_id}")
async def read_single_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books")
async def read_book_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


@app.get("/books_by_date/")
async def read_single_book(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return
