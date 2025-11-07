from pydantic import BaseModel, field_validator
from datetime import datetime, timezone
from typing import Optional, List
from schemas import WorkoutExerciseLogRead


class WorkoutSessionBase(BaseModel):
    date: int
    duration_minutes: Optional[float] = None
    weight_before: Optional[float] = None
    weight_after: Optional[float] = None
    notes: Optional[str] = None


class WorkoutSessionCreate(WorkoutSessionBase):
    user_id: int
    exercise_logs: List[WorkoutExerciseLogRead]


class WorkoutSessionRead(WorkoutSessionBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    exercise_logs: List[WorkoutExerciseLogRead] = []

    model_config = {"from_attributes": True}


class WorkoutSessionUpdate(BaseModel):
    date: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    weight_before: Optional[float] = None
    weight_after: Optional[float] = None
    notes: Optional[str] = None
    exercise_logs: Optional[List[WorkoutExerciseLogRead]] = None
