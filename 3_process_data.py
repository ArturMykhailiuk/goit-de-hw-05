from kafka import KafkaProducer, KafkaConsumer
from configs import kafka_config
import json
import uuid
import time
import random

# Створення Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    security_protocol=kafka_config['security_protocol'],
    sasl_mechanism=kafka_config['sasl_mechanism'],
    sasl_plain_username=kafka_config['username'],
    sasl_plain_password=kafka_config['password'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda v: json.dumps(v).encode('utf-8')
)

consumer = KafkaConsumer(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    security_protocol=kafka_config['security_protocol'],
    sasl_mechanism=kafka_config['sasl_mechanism'],
    sasl_plain_username=kafka_config['username'],
    sasl_plain_password=kafka_config['password'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    key_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',  # Зчитування повідомлень з початку
    enable_auto_commit=True,       # Автоматичне підтвердження зчитаних повідомлень
    group_id='my_consumer_group_3'   # Ідентифікатор групи споживачів
)
my_name = "artur_home"
building_sensors = f'{my_name}_building_sensors'
consumer.subscribe([building_sensors])

def process_data():
    try:
        for message in consumer:
            print(f"Received message: {message.value} with key: {message.key}, partition {message.partition}")
            print("-----------------------------------------------------------------------------------------")
            data = json.loads(message.value)
            sensor_id = data['sensor_id']
            temperature = data['temperature']
            humidity = data['humidity']
            timestamp = data['timestamp']

            if temperature > 40:
                print (f"Message with key:{message.key} will be send to {my_name}_temperature_alerts")
                alert = {
                    'sensor_id': sensor_id,
                    'timestamp': timestamp,
                    'temperature': temperature,
                    'message': 'Temperature exceeds 40°C'
                }
                producer.send(f'{my_name}_temperature_alerts', key=str(sensor_id), value=json.dumps(alert))
                producer.flush()
                print(f"Sent temperature alert to {my_name}_temperature_alerts: {alert}")
                print ("---------------------------------------------------------------")

            if humidity > 80 or humidity < 20:
                print(f"Message with key:{message.key} will be send to {my_name}_humidity_alerts")
                alert = {
                    'sensor_id': sensor_id,
                    'timestamp': timestamp,
                    'humidity': humidity,
                    'message': 'Humidity out of range (20-80%)'
                }
                producer.send(f'{my_name}_humidity_alerts', key=str(sensor_id), value=json.dumps(alert))
                producer.flush()
                print(f"Sent temperature alert to {my_name}_humidity_alerts: {alert}")
                print ("---------------------------------------------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        consumer.close()
        producer.flush()
        producer.close()

if __name__ == "__main__":
    process_data()




