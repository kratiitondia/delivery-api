import os
from flask import Flask, request, jsonify
from logic import calculate_minimum_cost

from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 

@app.route('/calculate-cost', methods=['POST'])
def calculate_cost():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request"}), 400
    cost = calculate_minimum_cost(data)
    return jsonify({"minimum_cost": cost})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
