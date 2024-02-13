from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Response(BaseModel):
    message: str
    status_code: int

class User(BaseModel):
    username: str
    password: str

@router.post("/register/", response_model=Response)
async def create_item(item: User):


    


    return item
