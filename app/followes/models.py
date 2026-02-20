from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float , TIMESTAMP , text , ForeignKey 
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey("users.id"))
    following_id = Column(Integer, ForeignKey("users.id"))