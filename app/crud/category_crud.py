from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate

class CategoryCRUD:
    def create_category(self, db: Session, category: CategoryCreate):
        db_category = Category(name=category.name, description=category.description)
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    
category = CategoryCRUD()