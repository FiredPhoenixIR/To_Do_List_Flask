'''
a simple example of a Flask API that serves as a basic "To-Do List" application with CRUD (Create, Read, Update, Delete) operations
'''

from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data (in-memory storage)
todos = [
    {"id": 1, "task": "Self Study -- Coursera Course"},
    {"id": 2, "task": "Work Out"},
    {"id": 3, "task": "Social App Cehcking"},
]

# Route to get all tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos})

# Route to get a specific task by ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({"todo": todo})

# Route to create a new task
@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Task is required"}), 400

    new_todo = {
        'id': len(todos) + 1,
        'task': request.json['task']
    }
    todos.append(new_todo)
    return jsonify({"todo": new_todo}), 201

# Route to update a task by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Task is required"}), 400

    todo['task'] = request.json['task']
    return jsonify({"todo": todo})

# Route to delete a task by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todos.remove(todo)
    return jsonify({"message": "Todo deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

# you can run the Flask application
# and it will expose the API endpoints at the specified routes (e.g., http://localhost:5000/todos). 
# You can interact with the API using tools like Postman or by sending HTTP requests directly
