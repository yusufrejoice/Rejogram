from fastapi import FastAPI , Response , status , HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from uuid import uuid4
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from sqlalchemy.orm import Session
from app import utils
from app.database import engine , SessionLocal 
from app.utils import pwd_context
from app.user import user
from app.like import like
from app.auth import auth
from app.followes import followes
from app.comment import comment
from app.post import post
from app.utils import get_db
from app.followes import models
from app.comment import models
from app.user import models



rejo = FastAPI()
models.Base.metadata.create_all(bind=engine)
rejo.include_router(followes.router)
rejo.include_router(user.router)
rejo.include_router(like.router)
rejo.include_router(comment.router)
rejo.include_router(utils.router)
rejo.include_router(auth.router)
rejo.include_router(post.router)