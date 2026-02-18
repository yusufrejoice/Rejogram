from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class singup_model (Base):
    __tablename__ = "singup1"

    id = Column(UUID(as_uuid=True) , primary_key=True,default=uuid.uuid4)
    name = Column(String , nullable=False)
    email = Column(String , unique =True ,nullable= False )
    password= Column(String,nullable=False)
    date_of_birth = Column(Date, nullable=False)
    passport_num = Column(Integer , primary_key=True,nullable=False)
    year = Column(Integer , nullable=False)
    is_active = Column(Boolean, default=True)
    is_block = Column(Boolean, default=False)
    city = Column(String , nullable=False)
    state = Column(String , nullable=False)
    contry = Column(String , nullable=False)