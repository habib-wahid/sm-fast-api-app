
from sqlalchemy.orm import Session
from app import models, schemas


class UserCRUD:
    def create_user(self, db:Session, user: schemas.UserCreate):
        db_user = models.User(email=user.email, username=user.username)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

user = UserCRUD()