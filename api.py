import os
from flask import Flask,request,Response,jsonify
from models import db,Person


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(BASE_DIR,'testdatabase.sqlite')

db.init_app(app)

@app.route('/create-person', methods = ['POST'])
def create_person():
    content = request.json
    person = Person(first_name = content['first_name'],
                last_name = content['first_name'],
                age = content['age'],
                email = content['email'])
    db.session.add(person);            
    db.session.commit()
    
    return jsonify(person)
    
@app.route('/get-all-persons',methods = ['GET'])
def get_all_persons():
    persons = Person.query.all()

    return jsonify(persons)

@app.route('/update-person',methods = ['PUT'])
def update_person():
    content = request.json
    person = db.session.query(Person).get(content['id'])
    
    if person is not None:
        person.first_name = content['first_name']
        person.last_name = content['last_name']
        person.age = content['age']
        person.email = content['email']

    db.session.commit() 
    return jsonify(person)


@app.route('/delete-person/<id>',methods = ['DELETE'])
def delete_person(id):
    person = db.session.query(Person).get(id)
    if  person is not None:
        db.session.delete(person)

    db.session.commit()
    return jsonify(person)


if __name__ == '__main__':
    app.run(debug = True) 