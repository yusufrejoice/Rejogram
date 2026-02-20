from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float , TIMESTAMP ,Text , ForeignKey
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import UUID


class comment(Base):
    __tablename__ = "comments"

    cmt_id = Column(Integer,primary_key=True, nullable=False )
    contant = Column(String,nullable=False)
    published = Column(Boolean,server_default= 'TRUE' ,nullable= False )
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default= text('now()'))
    post_id = Column(Integer,ForeignKey("posts.post_id", ondelete= "CASCADE"), nullable= False )
    owner_id = Column(Integer,ForeignKey("users.user_id", ondelete= "CASCADE"), nullable= False )