from flask import Flask, request, make_response
from flask_cors import CORS
from config import db, migrate
from models import Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
db.init_app(app)
migrate.init_app(app, db)

# A GET route to fetch all plants
@app.route('/plants', methods=['GET'])
def get_all_plants():
    plants = Plant.query.all()
    plant_list = [plant.to_dict() for plant in plants]
    return plant_list, 200

# A POST route to create a new plant
@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.json
    try:
        new_plant = Plant(
            name=data['name'],
            image=data['image'],
            price=data['price'],
            is_in_stock=data['is_in_stock']
        )
        db.session.add(new_plant)
        db.session.commit()
        return new_plant.to_dict(), 201
    except KeyError:
        return {'error': 'Missing required fields'}, 400
    except Exception as e:
        return {'error': str(e)}, 400

# A GET route to fetch a single plant by its ID
@app.route('/plants/<int:id>', methods=['GET'])
def get_plant_by_id(id):
    plant = db.session.get(Plant, id)
    if not plant:
        return {'error': 'Plant not found'}, 404
    return plant.to_dict(), 200

# A PATCH route to update a plant's stock status
@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return {'error': 'Plant not found'}, 404

    data = request.json
    try:
        if 'is_in_stock' in data:
            plant.is_in_stock = data['is_in_stock']
        db.session.commit()
        return plant.to_dict(), 200
    except Exception as e:
        return {'error': str(e)}, 400

# A DELETE route to remove a plant from the database
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = Plant.query.get(id)
    if not plant:
        return make_response("", 404)

    db.session.delete(plant)
    db.session.commit()
    return make_response("", 204)

if __name__ == '__main__':
    app.run(port=5555, debug=True)