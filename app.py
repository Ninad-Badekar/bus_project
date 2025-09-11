from flask import Flask, render_template, jsonify
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)

bus_data = {}

def consume_data():
    consumer = KafkaConsumer(
        "bus_location",
        bootstrap_servers="localhost:9092",
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
    for msg in consumer:
        bus = msg.value["bus_no"]
        bus_data[bus] = msg.value
        print("Consumed:", msg.value)

threading.Thread(target=consume_data, daemon=True).start()

@app.route("/")
def index():
    buses = list(bus_data.keys())
    return render_template("index.html", buses=buses)

@app.route("/bus/<bus_no>")
def get_bus(bus_no):
    data = bus_data.get(bus_no, {"error": "No data yet"})
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
