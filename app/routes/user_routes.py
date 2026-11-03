from fastapi import APIRouter
from fastapi import APIRouter
from app.core.exceptions import ApiException

router = APIRouter()

@router.get("/")
async def get_users():

    return {
        "success": True,
        "users": []
    }


router = APIRouter()

@router.get("/error")
async def test_error():

    raise ApiException(
        400,
        "Error de prueba"
    )
