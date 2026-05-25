from app.db.schema import User
from app.models import user_model
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid


class UserService:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def list_users(self) -> list[User]:
        result = await self._db.execute(select(User).order_by(User.created_at.desc()))
        users = [row[0] for row in result.all()]

        users_data = []
        for user in users:
            users_data.append(
                {
                    "id": str(user.id),
                    "username": user.username,
                    "cefr_level": user.cefr_level,
                    "native_language": user.native_language,
                    "interface_language": user.interface_language,
                    "learning_language": user.learning_language,
                    "created_at": user.created_at.isoformat()
                }
            )
        
        return users_data
    
    async def create_user(self, user: user_model.User) -> User:
        db_user = User(
            username = user.username,
            cefr_level = user.cefr_level,
            native_language = user.native_language,
            interface_language = user.interface_language,
            learning_language = user.learning_language
            )
        
        self._db.add(db_user)
        await self._db.commit()
        await self._db.refresh(db_user)

        return db_user
    
    async def update_user_name(self, user_id: str, user_name: str) -> User:
        uuid_user_id = uuid.UUID(user_id)
        query = await self._db.execute(select(User).where(User.id == uuid_user_id))
        user = query.scalars().first()
        user.user_name = user_name
        
        await self._db.commit()
        await self._db.refresh(user)

        return user