#  School Bus Tracker (Kafka + Flask + Leaflet)

#### This project lets parents track their kids’ school buses in real-time.
#### It uses Kafka for streaming bus GPS data, Flask for the backend, and Leaflet.js for live maps.

## Project Structure
```bash
bus_project/
│── app.py                # Flask app + Kafka consumer
│── generate_data.py       # Kafka producer (simulates bus GPS)
│── templates/
│    └── index.html        # UI with Leaflet map
│── README.md              # Documentation
|── dags/
     └── bus_pipeline_dag.py #For future scope

```
## Requirements

- #### **Python 3.8+**

- #### **Kafka** (with Zookeeper or KRaft mode)

- #### **pip** for Python packages

##  Installation

#### 1. Clone the repo / create folder
```bash
git clone <repo-url> bus_project
cd bus_project
```

#### 2. Install dependencies
```bash
pip3 install -r requirements.txt
```

#### 3. Start Kafka 
```bash
bin/kafka-server-start.sh config/server.properties
```

#### 4. Create Topic
```bash
bin/kafka-topics.sh --create --topic bus_location --bootstrap-server localhost:9092
```

## Running the Project

#### 1. Run Producer (simulate buses)
```bash
python3 generate_data.py
```

#### 2. Run Flask App
```bash
python3 app.py
```

#### 3. Open UI
**Visit → http://127.0.0.1:5000**
- Click Refresh Busses to load bus numbers.
-  Select Bus number and click Track bus
-  Watch Bus move live on time

## How It Works

- generate_data.py → Kafka Producer
    - Generates random lat/lon for buses

    - Sends JSON messages to bus_location topic

- app.py → Flask + Kafka Consumer

    - Background thread consumes Kafka messages

    - Stores the latest location for each bus

    - Serves an API /bus/<bus_no> for bus location

    - Renders UI (index.html)

- index.html → Leaflet.js Map

    - Dropdown to select a bus

    - Fetches bus location every 2s

    - Updates marker on OpenStreetMap