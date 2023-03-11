from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from core.config import settings

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True  # type: ignore
)
DBSession = Session(bind=engine, autoflush=False, autocommit=False)
