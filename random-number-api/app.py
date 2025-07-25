from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Random Indian Mobile Number API!"})

@app.route('/random')
def random_mobile_number():
    number = random.randint(1000000000, 9999999999)  # Ensures exactly 10 digits
    formatted_number = f"+91 {number}"
    return jsonify({"mobile_number": formatted_number})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
