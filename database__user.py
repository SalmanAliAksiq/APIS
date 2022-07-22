from flask import *
from flask_sqlalchemy import SQLAlchemy
from app1 import app
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
d = SQLAlchemy(app)


class User(d.Model):
    id = d.Column(d.Integer, primary_key = True)
    u_title = d.Column(d.String(40),nullable=False)
    u_role = d.Column(d.String(40),nullable=False)
    u_company = d.Column(d.String(40),nullable=False)
    u_university = d.Column(d.String(40),nullable=False)
    u_connections = d.Column(d.String(40),nullable=False)
    u_profile_url = d.Column(d.String(40),nullable=False)
    date_created = d.Column(d.DateTime,default = datetime.utcnow)
    
    
class UserData(d.Model, SerializerMixin):
    id = d.Column(d.Integer, primary_key = True)
    u_title = d.Column(d.String(40),nullable=False)
    u_role = d.Column(d.String(40),nullable=False)
    u_company = d.Column(d.String(40),nullable=False)
    u_university = d.Column(d.String(40),nullable=False)
    u_connections = d.Column(d.String(40),nullable=False)
    u_profile_url = d.Column(d.String(40),nullable=False)
    date_created = d.Column(d.DateTime,default = datetime.utcnow)
    
    