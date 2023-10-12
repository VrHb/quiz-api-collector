import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

PSQL_PASSWORD = os.getenv("PSQL_PASSWORD")
PSQL_DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://postgres:{PSQL_PASSWORD}@psdb/{PSQL_DB_NAME}"

engine = create_engine(
    DATABASE_URL 
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
