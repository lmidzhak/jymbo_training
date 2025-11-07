from typing import Any, Type, Sequence
from fastapi import HTTPException, status
from sqlalchemy import insert, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


class AsyncCRUD:
    """Generic asynchronous CRUD for any SQLAlchemy model using AsyncSession."""

    def __init__(self, model: Type):
        self.model = model

    async def create(self, db: AsyncSession, **kwargs) -> Any:
        """Create a new instance."""
        try:
            instance = self.model(**kwargs)
            db.add(instance)
            await db.commit()
            await db.refresh(instance)
            return instance
        except IntegrityError as e:
            await db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to create {self.model.__name__}",
            ) from e

    async def bulk_create(self, db: AsyncSession, objects: Sequence[dict]) -> None:
        """Insert multiple records at once."""
        await db.execute(insert(self.model).values(objects))
        await db.commit()

    async def read(self, db: AsyncSession, id_: Any) -> Any | None:
        """Get a single record by id."""
        result = await db.execute(select(self.model).where(self.model.id == id_))
        return result.scalars().one_or_none()

    async def update(self, db: AsyncSession, id_: Any, **kwargs) -> Any | None:
        """Update a record by id."""
        result = await db.execute(select(self.model).where(self.model.id == id_))
        instance = result.scalars().one_or_none()
        if not instance:
            return None
        for field, value in kwargs.items():
            setattr(instance, field, value)
        await db.commit()
        await db.refresh(instance)
        return instance

    async def delete(self, db: AsyncSession, id_: Any) -> bool:
        """Delete a record by id."""
        result = await db.execute(select(self.model).where(self.model.id == id_))
        instance = result.scalars().one_or_none()
        if not instance:
            return False
        await db.delete(instance)
        await db.commit()
        return True

    async def get_all(self, db: AsyncSession) -> list[Any]:
        """Return all records."""
        result = await db.execute(select(self.model))
        return result.scalars().all()

    async def get_all_by_field(self, db: AsyncSession, field_name: str, value: Any) -> list[Any]:
        """Return all records where field == value."""
        field = getattr(self.model, field_name)
        result = await db.execute(select(self.model).where(field == value))
        return result.scalars().all()

    async def get_by_field(self, db: AsyncSession, field_name: str, value: Any) -> Any | None:
        """Return one record where field == value."""
        field = getattr(self.model, field_name)
        result = await db.execute(select(self.model).where(field == value))
        return result.scalars().one_or_none()
