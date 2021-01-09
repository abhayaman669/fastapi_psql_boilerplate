"""
This is sample router file
"""
from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def greet():
    return {
        "status": "Success.",
        "message": "Hello World!"
    }