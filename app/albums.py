from fastapi import APIRouter, HTTPException, Depends

from app.schemas import AlbumCreate, AlbumResponse
from app.auth import admin_required


router = APIRouter(
    prefix="/albums",
    tags=["Albums"]
)


# Временное хранилище.
# Позже заменим на PostgreSQL.
albums = []

next_id = 1


@router.get("/", response_model=list[AlbumResponse])
def get_albums():
    return albums


@router.get("/{album_id}", response_model=AlbumResponse)
def get_album(album_id: int):
    for album in albums:
        if album["id"] == album_id:
            return album

    raise HTTPException(
        status_code=404,
        detail="Диск не найден"
    )


@router.post(
    "/",
    response_model=AlbumResponse,
    status_code=201
)
def create_album(
    data: AlbumCreate,
    user=Depends(admin_required)
):
    global next_id

    album = {
        "id": next_id,
        "title": data.title,
        "musician_id": data.musician_id,
        "price": data.price,
        "stock": data.stock
    }

    albums.append(album)
    next_id += 1

    return album


@router.put(
    "/{album_id}",
    response_model=AlbumResponse
)
def update_album(
    album_id: int,
    data: AlbumCreate,
    user=Depends(admin_required)
):
    for album in albums:
        if album["id"] == album_id:
            album["title"] = data.title
            album["musician_id"] = data.musician_id
            album["price"] = data.price
            album["stock"] = data.stock

            return album

    raise HTTPException(
        status_code=404,
        detail="Диск не найден"
    )


@router.delete("/{album_id}")
def delete_album(
    album_id: int,
    user=Depends(admin_required)
):
    for album in albums:
        if album["id"] == album_id:
            albums.remove(album)

            return {
                "message": "Диск удалён"
            }

    raise HTTPException(
        status_code=404,
        detail="Диск не найден"
    )