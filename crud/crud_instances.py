from crud.base import AsyncCRUD
from db import User, Exercise, WorkoutSession, WorkoutExerciseLog


user_crud = AsyncCRUD(User)
exercise_crud = AsyncCRUD(Exercise)
session_crud = AsyncCRUD(WorkoutSession)
log_crud = AsyncCRUD(WorkoutExerciseLog)
