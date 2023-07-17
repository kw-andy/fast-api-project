from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "les_freres_karamazov", "author": "Dostoievski", "category": "fiction"},
    {"title": "foundation", "author": "Assimov", "category": "science fiction"},
    {"title": "spin1", "author": "Wilson", "category": "science fiction"},
    {"title": "spin2", "author": "Wilson", "category": "science fiction"},
    {"title": "spin3", "author": "Wilson", "category": "science fiction"},
    {"title": "home_is_where_we_are_now", "author": "Wang", "category": "biography"},
    {"title": "legalism", "author": "Han Feizi", "category": "history"},
]


@app.get("/books/{book_author}")
async def read_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


# query
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# query
@app.get("/books_auth/")
async def read_author_by_query(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


# path
@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/all-books")
async def read_all_books():
    return BOOKS


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books-update")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/{book_title}/")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break






"""



@app.get("/books/")@app.get("/books")
async def read_all_books():
    return BOOKS
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

            
@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {'dynamic_param': dynamic_param}            
"""
