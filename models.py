from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Musician(Base):
    __tablename__ = "musicians"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    albums = relationship("Album", back_populates="musician")


class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class Album(Base):
    __tablename__ = "albums"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    release_year = Column(Integer)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, nullable=False, default=0)
    musician_id = Column(Integer, ForeignKey("musicians.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    musician = relationship("Musician", back_populates="albums")

    # Бизнес-правила (Check Constraints) на уровне Python
    __table_args__ = (
        CheckConstraint('price >= 0', name='check_price_positive'),
        CheckConstraint('stock_quantity >= 0', name='check_stock_positive'),
    )


class AlbumGenre(Base):
    __tablename__ = "album_genres"
    album_id = Column(Integer, ForeignKey("albums.id", ondelete="CASCADE"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)


class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    album_id = Column(Integer, ForeignKey("albums.id", ondelete="RESTRICT"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint('quantity > 0', name='check_sale_quantity'),
        CheckConstraint('total_price >= 0', name='check_sale_total_price'),
    )