from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.models.base import Base, TimestampMixin
from db.models.enums.muscle_group import MuscleGroup
from db.models.enums.equipment_type import EquipmentType


class Exercise(Base, TimestampMixin):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    muscle_group: Mapped[MuscleGroup] = mapped_column(
        Enum(MuscleGroup, name="muscle_group_enum"), nullable=False
    )
    equipment: Mapped[EquipmentType] = mapped_column(
        Enum(EquipmentType, name="equipment_enum"),
        nullable=False,
        default=EquipmentType.NONE
    )

    logs: Mapped[list["WorkoutExerciseLog"]] = relationship(
        "WorkoutExerciseLog",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )
