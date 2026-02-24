from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


REJOGRAM_DATABASE_URL = settings.REJOGRAM_DATABASE_URL


engine = create_engine(REJOGRAM_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()