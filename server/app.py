from flask import Flask, jsonify, request
from flask_cors import CORS

from src.db.db import connection
from src.services.todo_service import get_todos, create_todo, delete_todo


app = Flask(__name__)
CORS(app, origins="*")


@app.route("/api/todo", methods=['GET', 'POST'])
def todo_router():
    response = []
    if request.method == 'GET': 
        response = get_todos(connection)
    elif request.method == 'POST':
        response = create_todo(con=connection, data=request.get_data().decode('utf-8'))

    return jsonify(response)

@app.route("/api/todo/<int:id>", methods=['DELETE'])
def todo_delete(id):
    response = delete_todo(connection, id)

    return jsonify(response)
    
    