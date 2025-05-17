from fastapi import APIRouter

custom_router = APIRouter()

@custom_router.get("/custom/hello")
async def hello():
    return {"message": "Hello from custom route!"}
