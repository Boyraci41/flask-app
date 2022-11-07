from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
db = SQLAlchemy()

@dataclass
class Person(db.Model):
    id:int
    first_name:str
    last_name:str
    last_name:str
    age:int

    
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(100),nullable = False)
    last_name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),unique=True, nullable = False)
    age = db.Column(db.Integer)
     
    def to_json(self):
        return { "id": self.id,"first_name": self.first_name}