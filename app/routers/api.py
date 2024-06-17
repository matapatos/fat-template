"""
Holds REST API endpoints
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/api")
async def api_example():
    return {"message": "My api sample endpoint"}
