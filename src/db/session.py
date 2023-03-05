from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql://admin:admin@db:5432/techgo")
DBSession = Session(bind=engine, autoflush=False, autocommit=False)
