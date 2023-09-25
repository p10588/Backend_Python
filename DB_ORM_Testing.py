import os
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

sql = 'postgresql'
ip = os.getenv('DB_IP_PORT')
username = os.getenv('DB_USER_NAME')
password = os.getenv('DB_PASSWORD')
dbname = os.getenv('DB_NAME')

db_url = f'{sql}://{username}:{password}@{ip}/{dbname}'

engine = sqlalchemy.create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the database schema
Base.metadata.create_all(engine)

# Create a session to interact with the database 
Session = sessionmaker(engine)
session = Session()

# CREATE(INSERT)
new_user = User(name = 'John', age = 30 )
session.add(new_user)
session.commit()

# READ(SELECT)
user = session.query(User).filter_by(name = 'John').first()
print(f'UserID: {user.id}, Name: {user.name}, Age: {user.age}')

# UPDATE
user.age = 35
session.commit()
print(f'UserID: {user.id}, Name: {user.name}, Age: {user.age}')

#DELETE(DROP)
session.delete(user)
session.commit()

#Close Session
session.close()


try:
    connect = engine.connect()
    print('Connected To PostgreSQL Database')
    connect.close()
except Exception as e:
    print(f'Connect fail: {e}')

