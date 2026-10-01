from pydantic import BaseModel, Field


class MusicianCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    genre: str = Field(min_length=1, max_length=50)


class MusicianResponse(MusicianCreate):
    id: int


class AlbumCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    musician_id: int
    price: float = Field(gt=0)
    stock: int = Field(ge=0)


class AlbumResponse(AlbumCreate):
    id: int


class SaleCreate(BaseModel):
    album_id: int
    quantity: int = Field(gt=0)


class SaleResponse(BaseModel):
    id: int
    album_id: int
    quantity: int
    total_price: float