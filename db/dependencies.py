from sqlalchemy.ext.asyncio import AsyncSession
from db.session import db_facade

async def get_db_session() -> AsyncSession:
    async with db_facade.session() as session:
        yield session
