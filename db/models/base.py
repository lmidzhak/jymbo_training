from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    __abstract__ = True
    __table_args__ = {"schema": "gym"}


class TimestampMixin:
    created_at: Mapped[int] = mapped_column(BigInteger, nullable=False)
    updated_at: Mapped[int] = mapped_column(BigInteger, nullable=False)
