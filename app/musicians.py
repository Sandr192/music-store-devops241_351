from fastapi import APIRouter, HTTPException, Depends

from app.schemas import MusicianCreate, MusicianResponse
from app.auth import admin_required


router = APIRouter(
    prefix="/musicians",
    tags=["Musicians"]
)


# Временное хранилище.
# Позже заменим его на PostgreSQL.
musicians = []

next_id = 1


@router.get("/", response_model=list[MusicianResponse])
def get_musicians():
    return musicians


@router.get("/{musician_id}", response_model=MusicianResponse)
def get_musician(musician_id: int):
    for musician in musicians:
        if musician["id"] == musician_id:
            return musician

    raise HTTPException(
        status_code=404,
        detail="Музыкант не найден"
    )


@router.post(
    "/",
    response_model=MusicianResponse,
    status_code=201
)
def create_musician(
    data: MusicianCreate,
    user=Depends(admin_required)
):
    global next_id

    musician = {
        "id": next_id,
        "name": data.name,
        "genre": data.genre
    }

    musicians.append(musician)
    next_id += 1

    return musician


@router.put(
    "/{musician_id}",
    response_model=MusicianResponse
)
def update_musician(
    musician_id: int,
    data: MusicianCreate,
    user=Depends(admin_required)
):
    for musician in musicians:
        if musician["id"] == musician_id:
            musician["name"] = data.name
            musician["genre"] = data.genre

            return musician

    raise HTTPException(
        status_code=404,
        detail="Музыкант не найден"
    )


@router.delete("/{musician_id}")
def delete_musician(
    musician_id: int,
    user=Depends(admin_required)
):
    for musician in musicians:
        if musician["id"] == musician_id:
            musicians.remove(musician)

            return {
                "message": "Музыкант удалён"
            }

    raise HTTPException(
        status_code=404,
        detail="Музыкант не найден"
    )