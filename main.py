import keyboard
import requests

# Flask
@app.route('/data', methods=['POST']) # pod methods nastavimo POST
def save_data():
    data = request.json
    return jsonify({"status": "saved"}) # tako, lahko tudi naš flask route vrne json

# Requests
keys = ['a', 'b', 'c']
response = requests.post('http://localhost:5000/data',
                        json={'keys': keys })