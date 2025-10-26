
from fastapi import FastAPI
from app.database import engine, Base
from app.api import users, category

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Menu API", version="1.0.0")

app.include_router(users.router, prefix="/api/v1")
app.include_router(category.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to the API"}