#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/')
def home():
    return """<a href="https://PythonRestSQLite.alpteja.repl.co/todo/api/v1.0/tasks">
    API_LINK
    </a>
    """
    # return "/todo/api/v1.0/tasks"

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5005)