from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from app.database import Base

category_item = Table(
    'category_item',
    Base.metadata,
    Column('category_id', ForeignKey('categories.id'), primary_key=True),
    Column('item_id', ForeignKey('items.id'), primary_key=True)
)

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)

    items = relationship(
        "Item",
        secondary=category_item,
        back_populates="categories"
    )