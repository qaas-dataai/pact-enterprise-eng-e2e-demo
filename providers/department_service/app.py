from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/department/42', methods=['GET'])
def department_42():
    return jsonify({'id': 42, 'name': 'Finance', 'code': 'FIN', 'disabled': False})

@app.route('/department/999', methods=['GET'])
def department_999():
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(port=5000)
