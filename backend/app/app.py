from fastapi import FastAPI
from app.routes import user, session, message
from app.db.schema import create_db_and_tables
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", # Vite React default
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(session.router)
app.include_router(message.router)

@app.get("/")
def get_test():
    return {"message": "Test"}