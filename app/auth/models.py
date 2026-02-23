from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float , TIMESTAMP , text , ForeignKey 
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class User (Base):
    __tablename__ = "user"

    user_id = Column(Integer,primary_key=True, nullable=False )
    username = Column(String , nullable=False)
    email = Column(String , unique = True ,nullable= False )
    password= Column(String,nullable=False)
    date_of_birth = Column(Date, nullable=False)


