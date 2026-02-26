import keyboard
import requests
import threading
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Flask route
@app.route('/data', methods=['POST'])  # Set POST method for this route
def save_data():
    data = request.json
    return jsonify({"status": "saved"})  # Return JSON response

# Function to start the Flask app in a separate thread
def start_flask():
    app.run(debug=True, use_reloader=False)  # `use_reloader=False` to prevent Flask from running twice

# Requests
keys = ['a', 'b', 'c']

# This will send a request after ensuring Flask is running
def send_request():
    response = requests.post('http://localhost:5000/data', json={'keys': keys})
    print(response.json())  # Print the response from Flask server

# Function that will run in a thread to send HTTP request
def send_request_in_thread():
    thread = threading.Thread(target=send_request)
    thread.start()

# Function that gets triggered when a key is pressed
def on_key_press(event):
    print(f'Key pressed: {event.name}')

# Register the function to "listen" for key presses
keyboard.on_press(on_key_press)

# Start Flask in a separate thread so it doesn't block the rest of the program
flask_thread = threading.Thread(target=start_flask)
flask_thread.start()

# Wait a bit to ensure Flask is running before sending requests
import time
time.sleep(1)  # Adjust this sleep time if necessary

# Send the POST request in a separate thread
send_request_in_thread()

# Program will keep running until ESC is pressed
keyboard.wait('esc')