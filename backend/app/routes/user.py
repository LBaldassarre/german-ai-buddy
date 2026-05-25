from fastapi import APIRouter, Depends
from app.models import user_model  
from app.services.user_service import UserService
from app.db.schema import async_session_maker

router = APIRouter()

def get_user_service() -> UserService:
    return UserService(session=async_session_maker())

@router.post("/create-user")
async def create_user(user: user_model.User, service: UserService = Depends(get_user_service)):
    return await service.create_user(user)

@router.get("/get-users")
async def get_users(service: UserService = Depends(get_user_service)):
    return await service.list_users()

@router.patch("/update_user_name/{user_id}")
async def update_user_name(user_id: str, user_name: str, service: UserService = Depends(get_user_service)):
    return await service.update_user_name(user_id, user_name)