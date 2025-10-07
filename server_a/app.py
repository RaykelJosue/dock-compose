from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "SERVER A APP"

@app.route('/get-products')
def get_products():
    try:
        response = requests.get("http://server_b:5000/products")
        data = response.json()
    except Exception as e:
        data = {"error": str(e)}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
