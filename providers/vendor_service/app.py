from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/vendor/22', methods=['GET'])
def vendor_22():
    return jsonify({'id': 22, 'name': 'VendorX', 'active': True, 'contact': 'vendor@example.com', 'terms': 'Net 30'})

@app.route('/vendor/999', methods=['GET'])
def vendor_999():
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(port=5000)
