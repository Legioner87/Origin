from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Books(Base):
    __tablename__ = "Books"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, unique=False, nullable=False, default="", server_default="")
    author_id = Column(Integer, ForeignKey("Authors.id"), nullable=False)

    authors = relationship("Authors", back_populates="books")