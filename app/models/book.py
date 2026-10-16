from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model):
    """class book inherits from db.Model from SQLAlchemy, 
    in SQLAlchemy constructor - we pass Base,
    in Base class, we get behavior from SQLAlchemy parent calss DeclarativeBase"""
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
