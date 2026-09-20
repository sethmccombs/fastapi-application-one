"""App One.

Provides a CRUD interface for managing a database of books
"""
from collections.abc import Generator
from datetime import datetime

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Base, Book, BookCreate

Base.metadata.create_all(bind=engine)
app = FastAPI()
router = APIRouter(prefix="/api/v1")

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/books")
async def read_books(db: Session = Depends(get_db)):
    result = db.scalars(select(Book)).all()
    return result

@router.get("/books/{item_id}")
async def read_book(item_id: int, db: Session = Depends(get_db)):
    statement = select(Book).where(Book.id == item_id)
    book = db.scalars(statement).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/books")
async def create_book(body: BookCreate, db: Session = Depends(get_db)):
    book = Book(
        title=body.title,
        description=body.description,
        status=body.status,
        created_at=datetime.now(),
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.put("/books/{id}")
async def update_book(id: int, body: BookCreate, db: Session = Depends(get_db)):
    statement = select(Book).where(Book.id == id)
    book = db.scalars(statement).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    book.title = body.title
    book.description = body.description
    book.status = body.status
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@router.delete("/books/{id}")
async def delete_book(id: int, db: Session = Depends(get_db)):
    statement = select(Book).where(Book.id == id)
    book = db.scalars(statement).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return book

app.include_router(router)
