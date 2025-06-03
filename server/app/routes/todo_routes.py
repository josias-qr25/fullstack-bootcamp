from flask import Blueprint, request, jsonify
from app.models.todo import Todo
from app import db

todo_bp = Blueprint('todo', __name__, url_prefix='/api/todos')


@todo_bp.route('', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    result = [{
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    } for todo in todos]
    return jsonify(result), 200


@todo_bp.route('', methods=['POST'])
def create_todo():
    data = request.get_json()

    if not data or 'title' not in data or not isinstance(data['title'], str):
        return jsonify({"error": "Title is required and must be a string"}), 400

    new_todo = Todo(title=data['title'], completed=False)
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({
        "id": new_todo.id,
        "title": new_todo.title,
        "completed": new_todo.completed
    }), 201


@todo_bp.route('/<int:todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()

    if 'completed' in data:
        todo.completed = data['completed']
    if 'title' in data:
        todo.title = data['title']

    db.session.commit()

    return jsonify({
        "id": todo.id,
        "title": todo.title,
        "completed": todo.completed
    }), 200


@todo_bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted"}), 200
