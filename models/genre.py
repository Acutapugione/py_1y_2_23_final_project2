from dataclasses import dataclass
from . import Base
from sqlalchemy import Column, String, Integer

@dataclass
class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    def __str__(self)->str:
        return f"_{self.name.title()}_"
    