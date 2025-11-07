from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, String
from db.models.base import Base, TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

    # Relationship with workout sessions
    workouts: Mapped[list["WorkoutSession"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User id={self.id} username={self.username}>"