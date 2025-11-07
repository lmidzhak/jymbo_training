from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from crud.crud_instances import exercise_crud
from db.dependencies import get_db_session
from schemas import ExerciseCreate, ExerciseRead, ExerciseUpdate

router = APIRouter(prefix="/exercises", tags=["Exercises"])


@router.post("/", response_model=ExerciseRead, status_code=status.HTTP_201_CREATED)
async def create_exercise(exercise_in: ExerciseCreate, db: AsyncSession = Depends(get_db_session)):
    """Create a new exercise"""
    return await exercise_crud.create(db, **exercise_in.model_dump())


@router.get("/", response_model=list[ExerciseRead])
async def get_exercises(db: AsyncSession = Depends(get_db_session)):
    """Get all exercises"""
    return await exercise_crud.get_all(db)


@router.get("/{exercise_id}", response_model=ExerciseRead)
async def get_exercise(exercise_id: int, db: AsyncSession = Depends(get_db_session)):
    """Get a single exercise by ID"""
    exercise = await exercise_crud.read(db, exercise_id)
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    return exercise


@router.put("/{exercise_id}", response_model=ExerciseRead)
async def update_exercise(exercise_id: int, exercise_in: ExerciseUpdate, db: AsyncSession = Depends(get_db_session)):
    """Update an exercise"""
    exercise = await exercise_crud.update(db, exercise_id, **exercise_in.model_dump(exclude_unset=True))
    if not exercise:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    return exercise


@router.delete("/{exercise_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_exercise(exercise_id: int, db: AsyncSession = Depends(get_db_session)):
    """Delete an exercise"""
    deleted = await exercise_crud.delete(db, exercise_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found")
    return None
