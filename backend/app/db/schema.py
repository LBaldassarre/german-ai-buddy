import uuid
from datetime import datetime
from sqlalchemy import Column, Text, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

class Base (DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(Text, nullable=False, unique=True)
    cefr_level = Column(Text, default="NT") # CEFR = Common European Framework of Reference for Languages / NT = Not Tested
    native_language = Column(Text, nullable=False)
    interface_language = Column(Text, default=native_language)
    learning_language = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def update(self, usename: str):
        self.username = usename


class Session(Base):
    __tablename__= "sessions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Text, ForeignKey(User.id), nullable=False)
    topic = Column(Text)
    session_type = Column(Text) # session_type IN ('free_conversation','grammar_practice','roleplay','vocabulary_review', 'exam_prep', 'pronunciation', 'work_conversation')        ),
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime)
    duration_seconds = Column(Integer)

    def endSession(self, topic: str, session_type: str):
        self.topic = topic
        self.session_type = session_type
        self.ended_at = datetime.utcnow()
        self.duration_seconds = (datetime.utcnow() - self.started_at).total_seconds()

class Message(Base):
    __tablename__= "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Text, ForeignKey(User.id), nullable=False)
    session_id = Column(Text, ForeignKey(Session.id), nullable=False)
    role = Column(Text, ) # Nedd to implement restrictions role in [user, assitant, system]
    created_at = Column(DateTime, default=datetime.utcnow)


class Mistake(Base):
    __tablename__= "mistakes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Text, ForeignKey(User.id), nullable=False)
    session_id = Column(Text, ForeignKey(Session.id), nullable=False)
    message_id = Column(Text, ForeignKey(Message.id), nullable=False)
    original_text = Column(Text, nullable=False)
    corrected_text = Column(Text, nullable=False)
    category = Column(Text, nullable=False)
    # category IN (
    #     'article_gender',
    #     'case_declension',
    #     'word_order',
    #     'verb_conjugation',
    #     'tense',
    #     'preposition',
    #     'sentence_structure',
    #     'vocabulary',
    #     'spelling',
    #     'punctuation',
    #     'pronunciation',
    #     'style_naturalness'
    # )
    expanation = Column(Text)
    severity = Column(Integer, nullable=False) # Severite between 1 and 5
    # 1 = minor issue, meaning is fully clear
    # 2 = noticeable mistake, but communication is easy
    # 3 = important grammar mistake, meaning still understandable
    # 4 = meaning becomes unclear or unnatural
    # 5 = blocks communication or changes meaning
    created_at = Column(DateTime, default=datetime.utcnow)

class Vocabulary(Base):
    __tablename__= "vocabulary"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Text, ForeignKey(User.id), nullable=False)
    word = Column(Text, nullable=False)
    translation = Column(Text)
    exposure_count = Column(Integer, default=0)
    confidece_score = Column(Float, default=0)
    last_seen = Column(DateTime)

class SessionSummary(Base):
    __tablename__= "sessino_summaries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Text, ForeignKey(User.id), nullable=False)
    session_id = Column(Text, ForeignKey(Session.id), nullable=False)
    summary = Column(Text, nullable=False)
    strengths = Column(Text)
    weaknesses = Column(Text)
    suggested_focus = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)