from fastapi import APIRouter, status
from database.database import Base, engine, SessionLocal

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

#Login

def login():
    pass

def authenticate():
    pass
