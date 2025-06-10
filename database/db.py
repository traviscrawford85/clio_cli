# app/core/database.py
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Always use the absolute path inside your project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /home/sysadmin01/clio_cli/database
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'clio_tokens.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def initialize_database():
    Base.metadata.create_all(bind=engine)
