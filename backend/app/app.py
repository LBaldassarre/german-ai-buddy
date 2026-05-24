from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostTest, UserT, SessionEndT, MessageT, MistakeT, VocabularyT, SessionSummaryT
from app.db import create_db_and_tables, get_async_session, User, Session, Message, Mistake, Vocabulary, SessionSummary
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
import uuid
from datetime import datetime

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

@app.get("/get-session")
async def get_sessions( 
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(
        select(Session)
        .order_by(Session.started_at.desc())
    )

    sessions = [row[0] for row in result.all()]

    sessionss_data = []
    for item in sessions:
        sessionss_data.append(
            {
                "id": str(item.id),
                "user_id": item.user_id,
                "topic": item.topic,
                "session_type": item.session_type,
                "started_at": item.started_at.isoformat(),
                "ended_at": item.ended_at,
                "duration_seconds": item.duration_seconds
            }
        )
    
    return {"sessions": sessionss_data}

@app.post("/create-session")
async def create_session(
    user_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    db_user_session = Session(
        user_id = user_id
        )
    
    session.add(db_user_session)
    await session.commit()
    await session.refresh(db_user_session)

@app.patch("/update_user/{user_id}")
async def update_user(
    user_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    uuid_user_id = uuid.UUID(user_id)
    query = await session.execute(
        select(User).where(User.id == uuid_user_id)
    )
    user = query.scalars().first()
    user.update("lab")
    
    session.add(user)
    await session.commit()

@app.patch("/end-session/{session_id}")
async def end_session(
    session_id: str,
    session: AsyncSession = Depends(get_async_session)
):
    session_id_uuid = uuid.UUID(session_id)
    query = await session.execute(
        select(Session).where(Session.id == session_id_uuid)
    )
    current_session = query.scalars().first()
    current_session.endSession("TestTopic", "TestSessionType")

    session.add(current_session)
    await session.commit()