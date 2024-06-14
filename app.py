from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

sensor_data = []

@app.route('/', methods=['GET'])
def home():
    return "Ini Flask API"

@app.route('/sensor', methods=['POST'])
def sensor():
    date = datetime.now()
    data = request.json
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    sensor_data.append({
        "tempature": temperature,
        "humidity": humidity,
        "datetime": date
    })

    print(f"Received temperature: {temperature}, humidity: {humidity}")
    
    response = {
        "status": "success",
        "message": "Data received",
        "data": {
            "temperature": temperature,
            "humidity": humidity,
            "datetime": date
        }
    }
    
    return jsonify(response), 200

@app.route('/sensor', methods=['GET'])
def get_data():
    return jsonify(sensor_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)