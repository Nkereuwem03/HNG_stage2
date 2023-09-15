from API.models import Person
from flask import jsonify, request, Blueprint
from API.extensions import db
from jsonschema import validate
import jsonschema

schema = {
    "type": "object",
    "additionalProperties": {"type": "string"}
}


def validatejson(object_data):
    try:
        validate(instance=object_data, schema=schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'tests route'}), 200


@main.route('/api', methods=['POST'])
def create_person():
    data = request.json
    is_valid = validatejson(data)
    if is_valid:
        for key, value in data.items():
            new_name = Person(name=value)
            db.session.add(new_name)
            db.session.commit()
        return jsonify({'Message': 'Created Successfully'}), 200
    return jsonify({'Message': 'Create Error'}), 500


@main.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = db.session.get(Person, int(user_id))
    if person:
        return jsonify({'Name': person.name}), 200
    return jsonify({'Message': 'Not Found'}), 404


@main.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = db.session.get(Person, int(user_id))
    if person:
        data = request.json
        if validatejson(data):
            for key, value in data.items():
                person.name = value
                db.session.commit()
            return jsonify({'Message': 'Update Successful'}), 200
        return jsonify({'Message': "Update Error"}), 500
    return jsonify({'Message': 'Not Found'}), 404


@main.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = db.session.get(Person, int(user_id))
    if person:
        db.session.delete(person)
        db.session.commit()
        return jsonify({'Message': 'Deleted Successfully'}), 200
    return jsonify({'Message': 'Not Found'}), 404
