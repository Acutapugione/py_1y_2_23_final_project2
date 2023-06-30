from sqlalchemy import text
from db import session, Genre, Film, select, update

films = session.scalars(select(Film)).fetchall()
print(films)
# sql =  select(Film)\
#         .where(Film.year > 2010)\
#         .where(Film.genre_id == 2)
        
# films_after_2010 = session.scalars(sql).first()
# print(films_after_2010)
author_name = 'Еріх'
films = (
    session.execute(select(Film).from_statement(text(f"select * from films where author like '%{author_name}%'")))
    .scalars()
    .all()
)

# films = session.scalars( 
#                 select(Film)\
#                 .where(Film.author.like(author_name)))\
#                 .fetchall()
print(films)
