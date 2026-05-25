from fastapi import FastAPI
from app.routes import user, session
from app.db.schema import create_db_and_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(session.router)

@app.get("/")
def get_test():
    return {"message": "Test"}