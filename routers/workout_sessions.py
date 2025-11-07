from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from crud.crud_instances import session_crud
from db.dependencies import get_db_session
from schemas import WorkoutSessionCreate, WorkoutSessionRead, WorkoutSessionUpdate


router = APIRouter(prefix="/workout-sessions", tags=["Workout Sessions"])


@router.post("/", response_model=WorkoutSessionRead, status_code=status.HTTP_201_CREATED)
async def create_workout_session(
    session_in: WorkoutSessionCreate,
    db: AsyncSession = Depends(get_db_session),
) -> WorkoutSessionRead:
    """Create a new workout session."""
    return await session_crud.create(db, **session_in.model_dump())


@router.get("/", response_model=List[WorkoutSessionRead])
async def get_workout_sessions(db: AsyncSession = Depends(get_db_session)) -> List[WorkoutSessionRead]:
    """Retrieve all workout sessions."""
    return await session_crud.get_all(db)


@router.get("/{session_id}", response_model=WorkoutSessionRead)
async def get_workout_session(session_id: int, db: AsyncSession = Depends(get_db_session)) -> WorkoutSessionRead:
    """Retrieve a single workout session by ID."""
    session = await session_crud.read(db, session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout session not found")
    return session


@router.put("/{session_id}", response_model=WorkoutSessionRead)
async def update_workout_session(
    session_id: int,
    session_in: WorkoutSessionUpdate,
    db: AsyncSession = Depends(get_db_session),
) -> WorkoutSessionRead:
    """Update a workout session."""
    session = await session_crud.update(db, session_id, **session_in.model_dump(exclude_unset=True))
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout session not found")
    return session


@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_workout_session(session_id: int, db: AsyncSession = Depends(get_db_session)) -> None:
    """Delete a workout session."""
    deleted = await session_crud.delete(db, session_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout session not found")
    return None
