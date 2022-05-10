# this allows us to use sqlalchemy object we created
from app import db 
class Cat(db.Model): # This is staying that Cats is a child class from db.Model
    # attributes will be columns, they are class variables rather than instance variables
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    color = db.Column(db.String)
    human_id = db.Column(db.Integer, db.ForeignKey('human.id')) # connecting to human table; with cat as child
    human = db.relationship("Human", back_populates="cats") # cats is plural because it is the many in the one:many relationship

# The model was based on this class:
# class Cat:
#     def __init__(self, id, name, age, color):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.color = color