from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Movie(Base):
    __tablename__ = 'movie'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255))
    director: Mapped[str] = mapped_column(db.String(255))
    year: Mapped[int] = mapped_column(db.Integer)
    genres = mapped_column(relationship("Genre", back_populates="movie"))

class Genre(Base):
    __tablename__ = 'genre'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255))
    movie_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('movie.id'))
    movie = relationship("Movie", back_populates="genres")
