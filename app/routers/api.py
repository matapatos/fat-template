"""Holds REST endpoints"""

from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["API"])


@router.get("")
async def api_example():
    """Example of a REST endpoint"""
    return {"message": "My api sample endpoint"}
