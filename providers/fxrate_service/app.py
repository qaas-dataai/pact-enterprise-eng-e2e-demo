from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fxrate/USD', methods=['GET'])
def fxrate_USD():
    return jsonify({'currency': 'USD', 'rate': 1.23})

@app.route('/fxrate/XYZ', methods=['GET'])
def fxrate_XYZ():
    return jsonify({'error': 'Not found'})

@app.route('/fxrate/audit/USD', methods=['GET'])
def fxrate_audit_USD():
    return jsonify({'currency': 'USD', 'source': 'ECB', 'timestamp': '2024-05-27T12:00:00Z'})

@app.route('/fxrate/audit/XYZ', methods=['GET'])
def fxrate_audit_XYZ():
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(port=5000)
