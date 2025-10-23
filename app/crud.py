from sqlalchemy.orm import Session
import models, schemas

def create_user(db:Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
