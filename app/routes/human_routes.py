from flask import Blueprint, jsonify, request, abort, make_response
from app.models.human import Human
from app.models.cats import Cat
from app import db # gives access to sqlalchemy object

humans_bp = Blueprint("humans_bp", __name__, url_prefix="/humans")

@humans_bp.route("", methods=["POST"])
def create_human():
    request_body = request.get_json()
    new_human = Human(name=request_body['name'])
    db.session.add(new_human)
    db.session.commit()
    response = {'msg': f'successfully created {new_human.name} with {new_human.id}'}
    return jsonify(response), 201

@humans_bp.route("", methods=['GET'])
def get_all_humans():
    humans = Human.query.all()
    response = []
    for human in humans:
        response.append({
            'name': human.name
        })
    return jsonify(response), 200

# helper function
def validate_human(human_id):
    try:
        human_id = int(human_id)
    except:
        abort(make_response({'msg': "Please give valid human id"}, 400))

    human = Human.query.get(human_id)
    if not human:
        abort(make_response({'msg': "Human with id# {human_id} not found"}, 404))
    return human


# example request body: {"name": "Catty", "color": "Tuxedo", "age": 10}
@humans_bp.route("/<human_id>/cats", methods=['POST'])
def create_cat_with_human(human_id):
    request_body = request.get_json()
    human = validate_human(human_id) # this includes checking for valid id, finding human with that id, and returning the human

    new_cat = Cat(
        name = request_body['name'],
        color = request_body['color'],
        age = request_body['age'],
        human = human)

    db.session.add(new_cat)
    db.session.commit()
    response = {
        'msg': f'New cat: {new_cat.name} created with owner {human.name}'}
    return jsonify(response), 201

@humans_bp.route("/<human_id>", methods=["GET"])
def get_all_cats_for_human(human_id):
    human = validate_human(human_id) # this includes checking for valid id, finding human with that id, and returning the human
    cats = []
    for cat in human.cats:
        cats.append({
            'id': cat.id,
            'name': cat.name,
            'color': cat.color,
            'age': cat.age
        })
    return jsonify(cats), 200
