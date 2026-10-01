from fastapi import APIRouter, HTTPException, Depends

from app.schemas import SaleCreate, SaleResponse
from app.albums import albums
from app.auth import get_current_user, admin_required


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


sales = []

next_id = 1


@router.get(
    "/",
    response_model=list[SaleResponse]
)
def get_sales(
    user=Depends(admin_required)
):
    return sales


@router.post(
    "/",
    response_model=SaleResponse,
    status_code=201
)
def create_sale(
    data: SaleCreate,
    user=Depends(get_current_user)
):
    global next_id

    album = None

    for item in albums:
        if item["id"] == data.album_id:
            album = item
            break

    if album is None:
        raise HTTPException(
            status_code=404,
            detail="Диск не найден"
        )

    if album["stock"] < data.quantity:
        raise HTTPException(
            status_code=409,
            detail="Недостаточно товара на складе"
        )

    total_price = album["price"] * data.quantity

    album["stock"] -= data.quantity

    sale = {
        "id": next_id,
        "album_id": data.album_id,
        "quantity": data.quantity,
        "total_price": total_price
    }

    sales.append(sale)
    next_id += 1

    return sale