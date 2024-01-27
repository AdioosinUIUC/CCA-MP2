from flask import Flask, request, jsonify

app = Flask(__name__)

# Default seed value
seed_value = 0

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    global seed_value

    if request.method == 'POST':
        # Handle HTTP POST request
        data = request.get_json()
        if 'num' in data:
            # Update seed value with the provided number
            seed_value = data['num']
            return jsonify({"message": "Seed value updated successfully"})
        else:
            return jsonify({"error": "Invalid request. 'num' parameter not found in JSON body"}), 400

    elif request.method == 'GET':
        # Handle HTTP GET request
        return str(seed_value)

if __name__ == '__main__':
    # Run the Flask application on port 5000
    app.run(host='0.0.0.0', port=8080)
