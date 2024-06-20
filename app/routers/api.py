"""
Holds REST API endpoints
"""

from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["API"])


@router.get("")
async def api_example():
    return {"message": "My api sample endpoint"}
