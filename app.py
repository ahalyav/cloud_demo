from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route to check if the app is running
@app.route('/')
def hello_world():
    return "Hello, World!"

# A simple API that returns a JSON response
@app.route('/api/greet', methods=['GET'])
def greet_user():
    name = request.args.get('name', 'Guest')
    return jsonify(message=f"Hello, {name}!")

# A POST request example
@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify(message="Data received", data=data)

if __name__ == '__main__':
    app.run(debug=True)
