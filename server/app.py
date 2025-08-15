import os
from typing import Dict, List, Any, Optional
from flask import Flask, jsonify, Response, request
from models import init_db, db, Dog, Breed
from models.dog import AdoptionStatus

# Get the server directory path
base_dir: str = os.path.abspath(os.path.dirname(__file__))

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "dogshelter.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
init_db(app)

@app.route('/api/dogs', methods=['GET'])
def get_dogs() -> Response:
    query = db.session.query(
        Dog.id,
        Dog.name,
        Breed.name.label('breed')
    ).join(Breed, Dog.breed_id == Breed.id)

    # Optional filters
    breed_id: Optional[int] = request.args.get('breedId', type=int)
    breed_name: Optional[str] = request.args.get('breed', type=str)
    available_only: bool = request.args.get('available', default=False, type=lambda v: str(v).lower() in ['1','true','yes','on'])

    if breed_id is not None:
        query = query.filter(Dog.breed_id == breed_id)
    elif breed_name:
        query = query.filter(Breed.name == breed_name)

    if available_only:
        query = query.filter(Dog.status == AdoptionStatus.AVAILABLE)

    dogs_query = query.all()
    
    # Convert the result to a list of dictionaries
    dogs_list: List[Dict[str, Any]] = [
        {
            'id': dog.id,
            'name': dog.name,
            'breed': dog.breed
        }
        for dog in dogs_query
    ]
    
    return jsonify(dogs_list)

@app.route('/api/dogs/<int:id>', methods=['GET'])
def get_dog(id: int) -> tuple[Response, int] | Response:
    # Query the specific dog by ID and join with breed to get breed name
    dog_query = db.session.query(
        Dog.id,
        Dog.name,
        Breed.name.label('breed'),
        Dog.age,
        Dog.description,
        Dog.gender,
        Dog.status
    ).join(Breed, Dog.breed_id == Breed.id).filter(Dog.id == id).first()
    
    # Return 404 if dog not found
    if not dog_query:
        return jsonify({"error": "Dog not found"}), 404
    
    # Convert the result to a dictionary
    dog: Dict[str, Any] = {
        'id': dog_query.id,
        'name': dog_query.name,
        'breed': dog_query.breed,
        'age': dog_query.age,
        'description': dog_query.description,
        'gender': dog_query.gender,
        'status': dog_query.status.name
    }
    
    return jsonify(dog)

# Route to get all breeds
@app.route('/api/breeds', methods=['GET'])
def get_breeds() -> Response:
    breeds_query = db.session.query(Breed).all()
    breeds_list = [{'id': breed.id, 'name': breed.name} for breed in breeds_query]
    return jsonify(breeds_list)

if __name__ == '__main__':
    app.run(debug=True, port=5100, host='0.0.0.0') # Listen on all interfaces for Codespaces compatibility - port 5100 to avoid macOS conflicts