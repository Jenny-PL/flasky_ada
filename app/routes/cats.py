from flask import Blueprint, jsonify, request
from app.models.cats import Cat
from app import db # gives access to sqlalchemy object

# convention to name blueprint with name_bp
# Blueprint(string, location, routes pre-fix)
cats_bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@cats_bp.route('', methods = ["POST"])
def create_one_cat():
    request_body = request.get_json()
    new_cat = Cat(name=request_body['name'],
                   age = request_body['age'],
                   color= request_body['color'])
    db.session.add(new_cat) # like staging changes in git
    db.session.commit()    # like in git, now commit the changes
    return {
        'id': new_cat.id,
        'msg': f'Sucessfully create cate with id {new_cat.id}'
    }, 201

@cats_bp.route('', methods= ['GET'])
def get_all_cats():
    cats = Cat.query.all()
    cats_response = []
    for cat in cats:
        cats_response.append({
            'id':cat.id,
            'name': cat.name,
            'age': cat.age,
            'color': cat.color
            })
    return jsonify(cats_response), 200

# class Cat:
#     def __init__(self, id, name, age, color):
#         self.id = id
#         self.name = name
#         self.age = age
#         self.color = color

# cats = [
#     Cat(1, 'Tanner', 7, 'orange'),
#     Cat(2, "Simba", 5, 'black'),
#     Cat(3, 'Chidi', 3, 'brown')
# ]

# @cats_bp.route("", methods=['GET'])
# def get_all_cats():
#     cat_response = []
#     for cat in cats:
#         cat_response.append({
#             'id':cat.id,
#             'name': cat.name,
#             'age': cat.age,
#             'color': cat.color
#             })
#     return jsonify(cat_response)

@cats_bp.route("/<cat_id>", methods=["GET"])
def get_one_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        response = {"msg": f"Invalid id: {cat_id}.  Need a cat id number"}
        return jsonify(response), 400

    chosen_cat = Cat.query.get(cat_id) # this replaced the for loop: for cat in cats
    if chosen_cat is None:
        response = {'msg': f"Could not find a cat with id {cat_id}"}
        return jsonify(response), 404
    response = {
            'id':chosen_cat.id,
            'name': chosen_cat.name,
            'age': chosen_cat.age,
            'color': chosen_cat.color
            }
    return jsonify(response), 200

@cats_bp.route("/<cat_id>", methods=["PUT"]) 
def update_one_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        response = {"msg": f"Invalid id: {cat_id}.  Need a cat id number"}
        return jsonify(response), 400

    chosen_cat = Cat.query.get(cat_id) # this replaced the for loop: for cat in cats
    if chosen_cat is None:
        response = {'msg': f"Could not find a cat with id {cat_id}"}
        return jsonify(response), 404
    try:
        request_body = request.get_json()
        chosen_cat.name = request_body['name']
        chosen_cat.age = request_body['age']
        chosen_cat.color = request_body['color']
        db.session.commit()
    except KeyError:
        return {'msg': f" Name, age, and color are required to update: cat #: {chosen_cat.id}"}, 400

    response = {
        f"Successfully updated cat #: {chosen_cat.id}: {chosen_cat.name}. New cat info as follows: "
            'id':chosen_cat.id,
            'name': chosen_cat.name,
            'age': chosen_cat.age,
            'color': chosen_cat.color
            }

    return jsonify(response), 200

@cats_bp.route("/<cat_id>", methods=["DELETE"])
def delete_cat(cat_id):
    try:
        cat_id = int(cat_id)
    except ValueError:
        response = {"msg": f"Invalid id: {cat_id}.  Need a cat id number"}
        return jsonify(response), 400

    chosen_cat = Cat.query.get(cat_id) # this replaced the for loop: for cat in cats
    if chosen_cat is None:
        response = {'msg': f"Could not find a cat with id {cat_id}"}
        return jsonify(response), 404
    
    db.session.delete(chosen_cat)
    db.session.commit()
    response = {
        'msg': f'Successfully deleted : {chosen_cat}'
    }
    return jsonify(response), 200