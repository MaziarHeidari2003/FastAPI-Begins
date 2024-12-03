from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from src.config import Config

DATABASE_URL = f"postgresql+asyncpg://{Config.DATABASE_USER}:{Config.DATABASE_PASSWORD}@{Config.DATABASE_HOST}:{Config.DATABASE_PORT}/{Config.DATABASE_NAME}"

async_engine = create_async_engine(url=DATABASE_URL,echo=True)

async def init_db():
    async with async_engine.begin() as conn:
        statement = text("SELECT 'hello'")
        result = await conn.execute(statement)
        print(result.all())