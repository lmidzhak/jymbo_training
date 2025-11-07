from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from crud.crud_instances import log_crud
from db.dependencies import get_db_session
from schemas import (
    WorkoutExerciseLogCreate,
    WorkoutExerciseLogRead,
    WorkoutExerciseLogUpdate,
)

router = APIRouter(prefix="/workout-logs", tags=["Workout Exercise Logs"])


@router.post("/", response_model=WorkoutExerciseLogRead, status_code=status.HTTP_201_CREATED)
async def create_log(log_in: WorkoutExerciseLogCreate, db: AsyncSession = Depends(get_db_session)):
    """Create a new workout exercise log."""
    return await log_crud.create(db, **log_in.model_dump())


@router.get("/", response_model=List[WorkoutExerciseLogRead])
async def get_logs(db: AsyncSession = Depends(get_db_session)):
    """Get all workout exercise logs."""
    return await log_crud.get_all(db)


@router.get("/{log_id}", response_model=WorkoutExerciseLogRead)
async def get_log(log_id: int, db: AsyncSession = Depends(get_db_session)):
    """Get a single workout exercise log by ID."""
    log = await log_crud.read(db, log_id)
    if not log:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log not found")
    return log


@router.put("/{log_id}", response_model=WorkoutExerciseLogRead)
async def update_log(log_id: int, log_in: WorkoutExerciseLogUpdate, db: AsyncSession = Depends(get_db_session)):
    """Update a workout exercise log."""
    updated = await log_crud.update(db, log_id, **log_in.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log not found")
    return updated


@router.delete("/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_log(log_id: int, db: AsyncSession = Depends(get_db_session)):
    """Delete a workout exercise log."""
    deleted = await log_crud.delete(db, log_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Log not found")
    return None
