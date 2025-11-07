from sqlalchemy import BigInteger, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.models.base import Base, TimestampMixin


class WorkoutSession(Base, TimestampMixin):
    __tablename__ = "workout_sessions"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("gym.users.id"), nullable=False)
    date: Mapped[int] = mapped_column(BigInteger, nullable=False)
    duration_minutes: Mapped[int | None] = mapped_column(Float, nullable=True)
    weight_before: Mapped[float | None] = mapped_column(Float, nullable=True)
    weight_after: Mapped[float | None] = mapped_column(Float, nullable=True)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)

    user = relationship("User", back_populates="workouts")
    exercise_logs = relationship(
        "WorkoutExerciseLog",
        back_populates="session",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<WorkoutSession id={self.id} user_id={self.user_id} date={self.date:%Y-%m-%d}>"
