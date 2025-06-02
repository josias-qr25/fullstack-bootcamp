from flask import Blueprint, current_app, request, jsonify, abort
from app import db
from app.models.todo import Todo
from app.services.schemas import TodoSchema
from flasgger import swag_from

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/todos', methods=['GET'])
@swag_from({
    'tags': ['Todos'],
    'summary': 'Get all todos',
    'description': 'Returns a list of all Todo items.',
    'responses': {
        200: {
            'description': 'A list of todos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'description': {'type': 'string'},
                        'completed': {'type': 'boolean'},
                        'created_at': {'type': 'string', 'format': 'date-time'}
                    }
                }
            }
        }
    }
})
def get_all_todos():
    try:
        #raise ValueError("Testing error logging")
        query = Todo.query

        # Filtering
        completed = request.args.get('completed')
        if completed is not None:
            query = query.filter(Todo.completed == (completed.lower() == 'true'))

        title = request.args.get('title')
        if title:
            query = query.filter(Todo.title.ilike(f"%{title}%"))

        # Sorting
        sort_by = request.args.get('sort_by', 'created_at')
        order = request.args.get('order', 'desc')

        if sort_by in ['title', 'created_at']:
            column = getattr(Todo, sort_by)
            column = column.desc() if order == 'desc' else column.asc()
            query = query.order_by(column)

        # Pagination
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        pagination = query.paginate(page=page, per_page=per_page, error_out=False)
        todos = pagination.items

        return jsonify({
            'total': pagination.total,
            'pages': pagination.pages,
            'current_page': page,
            'per_page': per_page,
            'todos': [{
                'id': t.id,
                'title': t.title,
                'description': t.description,
                'completed': t.completed,
                'created_at': t.created_at.isoformat()
            } for t in todos]
        })

    except Exception as e:
        current_app.logger.error(f"Error in get_all_todos: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500

@todo_bp.route('/todos/<int:todo_id>', methods=['GET'])
@swag_from({
    'tags': ['Todos'],
    'summary': 'Get a single todo by ID',
    'parameters': [
        {
            'name': 'todo_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the todo to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Todo found',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'completed': {'type': 'boolean'},
                    'created_at': {'type': 'string', 'format': 'date-time'}
                }
            }
        },
        404: {'description': 'Todo not found'}
    }
})
def get_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    return jsonify({
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed,
        'created_at': todo.created_at.isoformat()
    })

@todo_bp.route('/todos', methods=['POST'])
@swag_from({
    'tags': ['Todos'],
    'summary': 'Create a new todo',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'completed': {'type': 'boolean'}
                },
                'required': ['title']
            }
        }
    ],
    'responses': {
        201: {'description': 'Todo created'},
        400: {'description': 'Validation error'}
    }
})
def create_todo():
    data = request.get_json()
    schema = TodoSchema()
    try:
        validated = schema.load(data)
    except Exception as err:
        return jsonify({'error': str(err)}), 400
    
    todo = Todo(
        title=data['title'],
        description=data.get('description', ''),
        completed=data.get('completed', False)
    )
    db.session.add(todo)
    db.session.commit()
    return jsonify({'message': 'Todo created', 'id': todo.id}), 201

@todo_bp.route('/todos/<int:todo_id>', methods=['PUT'])
@swag_from({
    'tags': ['Todos'],
    'summary': 'Update an existing todo',
    'parameters': [
        {
            'name': 'todo_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'completed': {'type': 'boolean'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Todo updated'},
        400: {'description': 'Validation error'},
        404: {'description': 'Todo not found'}
    }
})
def update_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    schema = TodoSchema(partial=True)
    try:
        validated = schema.load(data)
    except Exception as err:
        return jsonify({'error': str(err)}), 400

    for key, value in validated.items():
        setattr(todo, key, value)

    db.session.commit()
    return jsonify({'message': 'Todo updated'})

@todo_bp.route('/todos/<int:todo_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Todos'],
    'summary': 'Delete a todo by ID',
    'parameters': [
        {
            'name': 'todo_id',
            'in': 'path',
            'type': 'integer',
            'required': True
        }
    ],
    'responses': {
        200: {'description': 'Todo deleted'},
        404: {'description': 'Todo not found'}
    }
})
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted'})
