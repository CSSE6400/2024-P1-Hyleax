from flask import Blueprint, jsonify

api = Blueprint('api', __name__, url_prefix='/api/v1')

# api routes
@api.route('/health')
def health():
    return jsonify({"status":"ok"})

@api.route('/todos', methods=['GET'])
def get_todos():
    return "single todo returned"

@api.route('/todos', methods=['POST'])
def post_todos():
    return jsonify({
        "title":"An example Todo",
        "description": "This is an example todo"
    })

@api.route('/todo/<int:id>', methods=['GET'])
def get_single_todo(id):
    return f"todo item: {id}"

@api.route('/todo/<int:id>', methods=['PUT'])
def update_todos(id):
    return jsonify({
        "id": id,
        "status": "updated"
    })

@api.route('/todo/<int:id>', methods=['DELETE'])
def delete_todos(id):
    return f"todo deleted for {id}"