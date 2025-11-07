from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers.users import router as user_router
from routers.exercises import router as exercise_router
from routers.workout_sessions import router as workout_session_router
from routers.workout_exercise_logs import router as log_router
from db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting up... connecting to DB")
    async with engine.begin() as conn:

        await conn.run_sync(lambda conn: print("DB connected"))

    yield

    print("Shutting down... closing DB connection")
    await engine.dispose()


app = FastAPI(
    title="Gym Tracker API",
    description="API for managing users and workouts",
    version="1.0.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(user_router)
app.include_router(exercise_router)
app.include_router(workout_session_router)
app.include_router(log_router)


@app.get("/")
async def root():
    return {"message": "Gym Tracker API is running 🚀"}
