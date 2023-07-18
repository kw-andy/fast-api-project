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

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, mx_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS = [
    Book(1, "Fast API Udemy", "Robby", "A very nice book", 5),
    Book(2, "L'idiot", "Doestoievski", "Un grand livre", 5),
    Book(3, "Prison notebooks", "Gramsci", "La réflexion du 20ème siècle", 5),
    Book(4, "Dune", "Herbert", "Splendide", 5),
    Book(5, "Sur la route", "Kerouac", "La liberté !", 5),
    Book(6, "La route", "McFarrell", "Horrible pourtant poètique", 5),
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




