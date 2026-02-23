from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float , TIMESTAMP ,Text , ForeignKey
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.sql import text
from sqlalchemy.dialects.postgresql import UUID


class Like(Base):
    __tablename__ = "likes"

    user_id = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.post_id", ondelete="CASCADE"),
        primary_key=True
    )