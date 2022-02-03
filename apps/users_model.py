from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Text,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import DateTime

base=declarative_base()

class Users(base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(Text,nullable=False)
    password=Column(String(100),nullable=False)
