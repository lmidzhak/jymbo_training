from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from crud.crud_instances import user_crud
from db.dependencies import get_db_session
from schemas import UserCreate, UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db_session)):
    return await user_crud.create(db, **user_in.model_dump())


@router.get("/", response_model=list[UserRead])
async def get_users(db: AsyncSession = Depends(get_db_session)):
    return await user_crud.get_all(db)


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db_session)):
    user = await user_crud.read(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_db_session)):
    user = await user_crud.update(db, user_id, **user_in.model_dump())
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db_session)):
    deleted = await user_crud.delete(db, user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return None