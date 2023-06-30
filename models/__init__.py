from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    ...

from .film import Film
from .genre import Genre