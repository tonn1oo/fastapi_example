from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory='templates')


class Book:
    __slots__ = ['bid', 'name', 'author', 'year', 'count']

    def __init__(self, bid: int, name: str, author: str, year: int, count: int):
        self.bid = bid
        self.name = name
        self.author = author
        self.year = year
        self.count = count


books = [
    Book(1, 'Konan Varvar', 'unknown', 1999, 2),
    Book(2, 'Xyenan Varvar', 'unknown', 1998, 32),
    Book(3, 'Pizdevan Varvar', 'unknown', 1997, 44),
    Book(4, 'Vaiovan Varvar', 'unknown', 1996, 3),
    Book(5, 'Tritovan Varvar', 'unknown', 1995, 1),

]


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'books': books})


@app.get("/books/{book_id}")
def book(book_id: int, request: Request):
    target_book = None
    for b in books:
        if b.bid == book_id:
            target_book = b
            break
    if not target_book:
        raise HTTPException(status_code=404, detail='Book not found')
    return templates.TemplateResponse('index.html', {'request': request, 'book': target_book})
