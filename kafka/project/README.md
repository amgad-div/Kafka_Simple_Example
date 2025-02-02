# Kafka Producer-Consumer Example

This project demonstrates a simple Kafka setup with a Python producer and Java consumer.

## Project Structure
```
.
├── docker-compose.yml
├── producer/
│   ├── requirements.txt
│   └── producer.py
└── consumer/
    ├── pom.xml
    └── src/main/java/com/example/Consumer.java
```

## How to Run (on a local machine with Docker)

1. Start Kafka and Zookeeper:
   ```bash
   docker-compose up -d
   ```

2. Install Python dependencies and run producer:
   ```bash
   cd producer
   pip install -r requirements.txt
   python producer.py
   ```

3. Build and run Java consumer:
   ```bash
   cd consumer
   mvn clean package
   java -cp target/kafka-consumer-1.0-SNAPSHOT.jar com.example.Consumer
   ```

## Components

- **Producer (Python)**: Generates incremental numbers and sends them to Kafka
- **Consumer (Java)**: Reads numbers from Kafka and prints them
- **Kafka**: Message broker running in Docker
- **Zookeeper**: Required for Kafka coordination

## Notes

- The producer generates a new number every second
- The consumer prints each number it receives
- Both producer and consumer run indefinitely until stopped
- The topic "numbers" is automatically created on startup