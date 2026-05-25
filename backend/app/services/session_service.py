from app.db.schema import Session
from app.models import session_model
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import uuid


class SessionService:
    def __init__(self, session: AsyncSession):
        self._db = session

    async def list_sessions(self) -> list[Session]:
        result = await self._db.execute(
            select(Session)
            .order_by(Session.started_at.desc())
        )

        sessions = [row[0] for row in result.all()]

        sessions_data = []
        for session in sessions:
            sessions_data.append(
            {
                "id": str(session.id),
                "user_id": session.user_id,
                "topic": session.topic,
                "session_type": session.session_type,
                "started_at": session.started_at.isoformat(),
                "ended_at": session.ended_at,
                "duration_seconds": session.duration_seconds
            }
        )
    
        return sessions_data
    
    async def create_session(self, user_id: str) -> Session:
        db_user_session = Session(
            user_id = user_id
            )
        
        self._db.add(db_user_session)
        await self._db.commit()
        await self._db.refresh(db_user_session)

        return db_user_session

    async def end_session(self, session_id: str) -> Session:
        session_id_uuid = uuid.UUID(session_id)
        query = await self._db.execute(
            select(Session).where(Session.id == session_id_uuid)
        )
        session = query.scalars().first()
        session.endSession("TestTopic", "TestSessionType")

        self._db.add(session)
        await self._db.commit()

        return session