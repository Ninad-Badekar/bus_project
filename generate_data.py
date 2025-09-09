import time
import json
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="172.16.12.165:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

buses = ["BUS101", "BUS102", "BUS103"]

locations = {
    "BUS101": [18.5204, 73.8567],
    "BUS102": [18.5300, 73.8500],
    "BUS103": [18.5400, 73.8700]
}

while True:
    for bus in buses:
        lat, lon = locations[bus]

        lat += random.uniform(-0.001, 0.001)
        lon += random.uniform(-0.001, 0.001)
        locations[bus] = [lat, lon]

        data = {"bus_no": bus, "latitude": lat, "longitude": lon}
        producer.send("bus_location", value=data)
        print("Sent:", data)

    time.sleep(2)
