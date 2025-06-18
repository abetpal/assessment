from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Simple API key authentication
API_KEY = "Hello-World"  # Replace with a secure key. Secure the key in some vault and use or use oauth 2.0 or jwt based authentication

@app.before_request
def check_api_key():
    # Checks API key in headers
    if request.headers.get("X-API-Key") != API_KEY:
        abort(401)

@app.route("/")
def hello():
    return jsonify(message="Hello, World!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
