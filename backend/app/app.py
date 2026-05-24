from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostTest, UserT, SessionT, MessageT, MistakeT, VocabularyT, SessionSummaryT
from app.db import create_db_and_tables, get_async_session, User, Session, Message, Mistake, Vocabulary, SessionSummary
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

@asynccontextmanager
async def lifespan(FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def get_test():
    return {"message": "Test"}

@app.post("/post")
def post_test(post: PostTest) -> PostTest:
    return {"title": "Post Title", "content": "Post Content"}

@app.post("/create-user")
async def create_user(
    user: UserT,
    session: AsyncSession = Depends(get_async_session)
):
    db_user = User(
        username = user.username,
        cefr_level = user.cefr_level,
        native_language = user.native_language,
        interface_language = user.interface_language,
        learning_language = user.learning_language
        )
    
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

@app.get("/get-users")
async def get_users( 
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(
        select(User)
        .order_by(User.created_at.desc())
    )

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
    
    return {"users": users_data}