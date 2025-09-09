from kafka import KafkaProducer
import csv
import time
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def produce(csv_file="bus_data.csv"):
    while True:
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            rows = list(reader)[-1:]  
            for row in rows:
                producer.send("bus_locations", row)
                print("Produced:", row)
        time.sleep(2)

if __name__ == "__main__":
    produce()
