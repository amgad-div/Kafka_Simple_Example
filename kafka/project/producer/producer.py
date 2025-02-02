from kafka import KafkaProducer
import json
import time

def create_producer():
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )

def generate_numbers():
    producer = create_producer()
    number = 0
    
    try:
        while True:
            message = {'number': number}
            producer.send('numbers', value=message)
            print(f"Produced: {message}")
            number += 1
            time.sleep(1)
    except KeyboardInterrupt:
        producer.close()

if __name__ == "__main__":
    generate_numbers()