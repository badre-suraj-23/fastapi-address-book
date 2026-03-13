# Handles database connection setup using SQLAlchemy
# SQLite is used as the persistent storage for this application

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "sqlite:///./address.db"


# Create database engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread":False}
)

# Session  used in API endpoints
SessionLocal = sessionmaker(bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()