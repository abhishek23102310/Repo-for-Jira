from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    todo = {
        'id': len(todos) + 1,
        'title': data['title'],
        'completed': data.get('completed', False)
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    for todo in todos:
        if todo['id'] == id:
            if 'title' in data:
                todo['title'] = data['title']
            if 'completed' in data:
                todo['completed'] = data['completed']
            return jsonify({'message': 'Todo updated'})
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    new_todos = [t for t in todos if t['id'] != id]
    if len(new_todos) == len(todos):
        return jsonify({'error': 'Todo not found'}), 404
    todos = new_todos
    return jsonify({'message': 'Todo deleted'})

if __name__ == '__main__':
    app.run(debug=True)
