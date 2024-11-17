from kafka import KafkaConsumer
from configs import kafka_config
import json

# Створення Kafka Consumer
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

# Назва топіку
my_name = "artur_home"
temperature_alerts = f'{my_name}_temperature_alerts'
humidity_alerts = f'{my_name}_humidity_alerts'

consumer.subscribe([temperature_alerts, humidity_alerts])

# Function to display alerts
def display_alerts():
    try:
        for message in consumer:
            alert = json.loads(message.value)
            print(f"Received message: {alert['message']} with key: {message.key}, partition {message.partition}")
    except Exception as e:
            print(f"An error occurred: {e}")
    finally:
            consumer.close()

if __name__ == "__main__":
    display_alerts()

