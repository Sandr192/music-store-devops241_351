from fastapi import FastAPI

from app.musicians import router as musicians_router
from app.albums import router as albums_router
from app.sales import router as sales_router
from app.auth import router as auth_router


app = FastAPI(
    title="Музыкальный магазин",
    description="API для управления музыкальным магазином",
    version="1.0.0"
)


app.include_router(musicians_router)
app.include_router(albums_router)
app.include_router(sales_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "API музыкального магазина работает"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }