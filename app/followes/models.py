# from sqlalchemy import Column, Integer, String, Boolean ,Date  , text , ForeignKey  , ARRAY
# from sqlalchemy.sql.expression import null
# from app.database import Base
# import uuid
# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base



class Follow(Base):
    __tablename__ = "followers"

    follower_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    following_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )
    
