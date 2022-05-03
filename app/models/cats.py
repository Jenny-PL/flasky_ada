from app import db    # this allows us to use sqlalchemy object we created

class Cat(db.Model):
    # attributes will be columns, they are class variables rather than instance variables
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    color = db.Column(db.String)

# The model was based on this class:
# class Cat:
#     def __init__(self, id, name, age, color):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.color = color