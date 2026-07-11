from fastapi import APIRouter

from app.services.database_service import database_service

router = APIRouter(prefix="/database", tags=["database"])


@router.get("/test")
def test_database_connection():
    response = database_service.client.table("test_connection").select("*").execute()

    return {
        "status": "connected",
        "data": response.data,
    }