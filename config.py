from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Load configuration from environment variables (.env file).
    Uses only one variable: DB_URL
    Example:
    DB_URL=postgresql+asyncpg://user:password@host:port/dbname
    """
    db_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def database_url(self) -> str:
        """Provide backward compatibility for Alembic and engine."""
        return self.db_url


settings = Settings()
