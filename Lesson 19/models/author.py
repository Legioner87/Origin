from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Authors(Base):
    __tablename__ = "Authors"
    id = Column(Integer, primary_key=True)
    name = Column(String(16), unique=True)

    books = relationship("Books", back_populates="authors")