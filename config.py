from pydantic_settings import BaseSettings
from urllib.parse import quote_plus


class Settings(BaseSettings):
    # Base env vars (can be in .env)
    db_type: str = "postgresql"
    db_user: str | None = None
    db_pass: str | None = None
    db_host: str | None = "localhost"
    db_port: str | None = "5432"
    db_name: str | None = "gym_db"
    use_sqlite: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def database_url(self) -> str:
        """
        Build a safe connection string for SQLAlchemy async engine.
        Automatically encodes special symbols in password.
        Fallbacks to SQLite if use_sqlite=True.
        """
        if self.use_sqlite or not self.db_user:
            return "sqlite+aiosqlite:///./local.db"

        password = quote_plus(self.db_pass or "")
        return (
            f"{self.db_type}+asyncpg://{self.db_user}:{password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()
