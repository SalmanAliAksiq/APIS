from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy_serializer import SerializerMixin


db = create_engine('postgresql://qyzfldnbruuurp:b302ab9d2122480b5b670330469dcb4e585671e89778216e3f6f2ff033b32d26@ec2-3-219-52-220.compute-1.amazonaws.com:5432/d60shomks5uoek')
base = declarative_base(db)
Session = sessionmaker(bind = db)
session = Session()


# class UserData(base):
#     __tablename__ = 'userInformation'
#     id = Column(Integer,primary_key = True)
#     user_name = Column(String,nullable = False)
#     user_role = Column(String,nullable = False)
#     user_company = Column(String,nullable = False)
#     user_university = Column(String,nullable = False)
#     user_connections = Column(String,nullable = False)
#     user_profile_link = Column(String,nullable = False)
    

class UserInfo(base,SerializerMixin):
    __tablename__ = 'userData'
    
    serialize_rules = ('-user_company',)

    id = Column(Integer,primary_key = True)
    user_name = Column(String,nullable = False)
    user_role = Column(String,nullable = False)
    user_company = Column(String,nullable = False)
    user_university = Column(String,nullable = False)
    user_connections = Column(String,nullable = False)
    user_profile_link = Column(String,nullable = False)
    date_created = Column(DateTime(),default = datetime.utcnow())
    
    

    
#base.metadata.create_all(db)

