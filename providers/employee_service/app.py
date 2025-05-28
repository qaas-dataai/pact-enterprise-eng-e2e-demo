from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/employee/1', methods=['GET'])
def employee_1():
    return jsonify({'id': 1, 'name': 'Alice', 'role': 'Engineer'})

@app.route('/employee/2', methods=['GET'])
def employee_2():
    return jsonify({'id': 2, 'name': 'Bob', 'role': 'HR Manager', 'department': 'HR'})

@app.route('/employee/404', methods=['GET'])
def employee_404():
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(port=5000)
