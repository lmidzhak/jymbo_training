from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from config import settings


engine = create_async_engine(settings.db_url, echo=True)
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class DBFacade:
    def __init__(self, session_factory):
        self._session_factory = session_factory

    @asynccontextmanager
    async def session(self) -> AsyncSession:
        """Async context manager for DB sessions."""
        session = self._session_factory()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


db_facade = DBFacade(async_session_factory)
