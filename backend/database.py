from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from fastapi import Depends

DATABASE_URL = "sqlite:///./test.db"  # SQLite local file for dev, use postgresql://user:pass@host/dbname for production

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # Needed only for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
metadata = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

