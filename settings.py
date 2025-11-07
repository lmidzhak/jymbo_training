from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "postgresql")
DB_USER = os.getenv("DB_USER")
DB_PASS = quote_plus(os.getenv("DB_PASS", ""))
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "gym_db")

database_url = f"{DB_TYPE}+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
