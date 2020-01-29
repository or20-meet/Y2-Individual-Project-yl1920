from model import Base, User, Image


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///databases.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(username, name, password):
	new_user = User(username = username, name = name, password=password)
	session.add(new_user)
	session.commit()

def get_all_users():
	return session.query(User).all()

def get_user_by_id(id):
	return session.query(User).filter_by(id=id).first()

def get_user_by_username(username):
	return session.query(User).filter_by(username=username).first()

def add_image(user_id, url):
	new_image = Image(user_id = user_id, url=url) 
	session.add(new_image)
	session.commit()

def images_by_id(id):
	return session.query(Image).filter_by(user_id = id).all()

def get_all_images():
	return session.query(Image).all()