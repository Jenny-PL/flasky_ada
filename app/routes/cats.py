from flask import Blueprint, jsonify

class Cat:
    def __init__(self, id, name, age, color):
        self.id = id
        self.name = name
        self.age = age
        self.color = color

cats = [
    Cat(1, 'Tanner', 7, 'orange'),
    Cat(2, "Simba", 5, 'black'),
    Cat(3, 'Chidi', 3, 'brown')
]

# convention to name blueprint with name_bp
# Blueprint(string, location, routes pre-fix)
cats_bp = Blueprint('cats_bp', __name__, url_prefix='/cats')

@cats_bp.route("", methods=['GET'])
def get_all_cats():
    cat_response = []
    for cat in cats:
        cat_response.append({
            'id':cat.id,
            'name': cat.name,
            'age': cat.age,
            'color': cat.color
            })
    return jsonify(cat_response)
