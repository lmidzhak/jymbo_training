from sqlalchemy import BigInteger, Float, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.models.base import Base, TimestampMixin


class WorkoutExerciseLog(Base, TimestampMixin):
    __tablename__ = "workout_exercise_logs"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("gym.workout_sessions.id"), nullable=False)
    exercise_id: Mapped[int] = mapped_column(ForeignKey("gym.exercises.id"), nullable=False)
    sets: Mapped[int] = mapped_column(Integer, nullable=False, default=3)
    reps: Mapped[int] = mapped_column(Integer, nullable=False, default=10)
    weight: Mapped[float | None] = mapped_column(Float, nullable=True)

    exercise = relationship("Exercise", back_populates="logs")
    session = relationship("WorkoutSession", back_populates="exercise_logs")

    def __repr__(self):
        return (
            f"<WorkoutExerciseLog session_id={self.session_id} "
            f"exercise_id={self.exercise_id} sets={self.sets} reps={self.reps} weight={self.weight}>"
        )
