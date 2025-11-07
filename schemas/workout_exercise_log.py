from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class WorkoutExerciseLogBase(BaseModel):
    exercise_id: int
    sets: int
    reps: int
    weight: Optional[float] = None


class WorkoutExerciseLogCreate(WorkoutExerciseLogBase):
    session_id: int


class WorkoutExerciseLogUpdate(BaseModel):
    sets: Optional[int] = None
    reps: Optional[int] = None
    weight: Optional[float] = None

    class Config:
        extra = "forbid"


class WorkoutExerciseLogRead(WorkoutExerciseLogBase):
    id: int
    session_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
