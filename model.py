from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key = True)
	username = Column(String)
	name = Column(String)
	password = Column(String)

class Image(Base):
	__tablename__ = 'images'
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer)
	url = Column(String)
	description = Column(String)


