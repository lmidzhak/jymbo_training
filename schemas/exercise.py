from typing import Optional
from enum import Enum
from schemas.base_schema import BaseModelWithTime


class MuscleGroup(str, Enum):
    CHEST = "CHEST"
    BACK = "BACK"
    SHOULDERS = "SHOULDERS"
    ARMS = "ARMS"
    LEGS = "LEGS"
    CORE = "CORE"
    FULL_BODY = "FULL_BODY"
    OTHER = "OTHER"


class Equipment(str, Enum):
    NONE = "NONE"
    BODYWEIGHT = "BODYWEIGHT"
    DUMBBELL = "DUMBBELL"
    BARBELL = "BARBELL"
    MACHINE = "MACHINE"
    KETTLEBELL = "KETTLEBELL"
    BAND = "BAND"
    CABLE = "CABLE"
    OTHER = "OTHER"

class ExerciseCreate(BaseModelWithTime):
    name: str
    muscle_group: MuscleGroup
    equipment: Equipment


class ExerciseUpdate(BaseModelWithTime):
    name: Optional[str] = None
    muscle_group: Optional[MuscleGroup] = None
    equipment: Optional[Equipment] = None


class ExerciseRead(ExerciseCreate):
    id: int

    model_config = {"from_attributes": True}
