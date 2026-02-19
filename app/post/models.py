from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float , TIMESTAMP , text , ForeignKey
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer,primary_key=True, nullable=False )
    tital = Column(String,nullable=False)
    contant = Column(String,nullable=False)
    published = Column(Boolean,server_default= 'TRUE' ,nullable= False )
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default= text('now()'))
    owner_id = Column(Integer,ForeignKey("users.user_id", ondelete= "CASCADE"), nullable= False )