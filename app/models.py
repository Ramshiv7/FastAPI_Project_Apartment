from sqlalchemy import Column, Integer, TIMESTAMP, Text, text 
from .database import Base


# DATABASE Model for Postgres

class DB(Base):
    __tablename__= 'owner_details'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text,nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(Text, nullable=False)
    paid_maintenance = Column(Text, nullable=False, server_default="False")
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))



class User(Base):
    __tablename__ = 'owner_logins'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_time = Column(TIMESTAMP, server_default=text('now()'))
