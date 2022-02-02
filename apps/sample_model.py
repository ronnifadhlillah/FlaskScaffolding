from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

base=declarative_base()

class MockData(base):
    __tablename__='mock_data'
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column(Text,nullable=False)
    last_name=Column(Text,nullable=False)
    email=Column(String(100),nullable=False)
    gender=Column(Text,nullable=False)
    ip_address=Column(String(50),nullable=False)
