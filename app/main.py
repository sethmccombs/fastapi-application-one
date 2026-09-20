"""App One.

Provides a CRUD interface for managing a database of books
"""
from datetime import datetime
from fastapi import HTTPException
from typing import Any


"""
Book
├── id
├── title
├── description
├── status
└── created_at
"""

from fastapi import FastAPI

app = FastAPI(root_path="/api/v1")

data = [
    {
        "id": 1,
        "title": "The Fellowship of the Ring",
        "description": "The first book in the Lord of the Rings trilogy",
        "status": "read",
        "created_at": datetime.now(),
    },
    {
        "id": 2,
        "title": "The Two Towers",
        "description": "The second book in the Lord of the Rings trilogy",
        "status": "read",
        "created_at": datetime.now(),
    },
]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def read_books():
    return {"books":  data}

@app.get("/books/{item_id}")
async def read_book(item_id: int):
    for book in data:
        if book.get("id") == item_id:
            return {"item_id": book}
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books")
async def create_book(body: dict[str, Any]):
    new = {
        "id": len(data) + 1,
        "title": body["title"],
        "description": body["description"],
        "status": body["status"],
        "created_at": datetime.now(),
    }

    data.append(new)
    return {"book": new}

@app.put("/books/{id}")
async def update_book(id: int, body: dict[str, Any]):
    for index, book in enumerate(data):
        if book.get("id") == id:
            updated = {
                "id": id,
                "title": body["title"],
                "description": body["description"],
                "status": body["status"],
                "created_at": book.get("created_at"),
            }
            data[index] = updated
            return {"book": updated}
    raise HTTPException(status_code=404, detail="Book not found")



@app.delete("/books/{id}")
async def delete_book(id: int):
    for index, book in enumerate(data):
        if book.get("id") == id:
            deleted = data.pop(index)
            return {"book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
