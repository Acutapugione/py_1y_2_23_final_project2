from dataclasses import dataclass
from . import Base
from models.genre import Genre
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship

@dataclass
class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name:str = Column(String)
    author: str = Column(String)
    genre: Mapped[Genre] = relationship()
    # genre: Genre = relationship(Genre, back_populates="film")
    genre_id: int = Column(ForeignKey(Genre.id, ondelete="CASCADE"))
    year: int = Column(Integer)
    
    
    def __str__(self)->str:
        return f"Назва: *{self.name}*\nАвтор: __{self.author}__\nЖанр: {self.genre}\nРік видання: {self.year}"
    