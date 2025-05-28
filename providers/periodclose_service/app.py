from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/period/2024Q1', methods=['GET'])
def period_2024Q1():
    return jsonify({'period': '2024Q1', 'status': 'closed', 'locked': True, 'month': 'March'})

@app.route('/period/invalid', methods=['GET'])
def period_invalid():
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(port=5000)
