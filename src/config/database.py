import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import DateTime, create_engine, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in the environment variables.")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
session_local = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
