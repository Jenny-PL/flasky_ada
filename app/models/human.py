# this allows us to use sqlalchemy object we created
from app import db 

class Human(db.Model): # This is staying that Cats is a child class from db.Model
    # attributes will be columns, they are class variables rather than instance variables
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    cats = db.relationship("Cat", back_populates="human") # human is singular because it is the one in the one:many relationship



