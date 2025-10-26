
from fastapi import APIRouter, Depends
from app.schemas import CategoryCreate, CategoryResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app import crud

router = APIRouter()

@router.post("/categories/", response_model=CategoryResponse, status_code=201)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.category.create_category(db, category)
    return db_category