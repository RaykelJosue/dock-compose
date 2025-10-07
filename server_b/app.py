from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "SERVER B APP"

@app.route('/products')
def products():
    random_products = random.sample(data["products"], 5)
    return jsonify(random_products)

# Cargar datos desde data.json
with open("data.json") as f:
    data = json.load(f)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
