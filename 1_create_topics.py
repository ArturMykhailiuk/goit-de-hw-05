from kafka.admin import KafkaAdminClient, NewTopic
from configs import kafka_config

# Створення клієнта Kafka
admin_client = KafkaAdminClient(
    bootstrap_servers=kafka_config['bootstrap_servers'],
    security_protocol=kafka_config['security_protocol'],
    sasl_mechanism=kafka_config['sasl_mechanism'],
    sasl_plain_username=kafka_config['username'],
    sasl_plain_password=kafka_config['password']
)

# Визначення нових топіків
my_name = "artur_home"
building_sensors = f'{my_name}_building_sensors'
temperature_alerts = f'{my_name}_temperature_alerts'
humidity_alerts = f'{my_name}_humidity_alerts'
num_partitions = 2
replication_factor = 1

building_sensors_topic = NewTopic(name=building_sensors, num_partitions=num_partitions, replication_factor=replication_factor)
temperature_alerts_topic = NewTopic(name=temperature_alerts, num_partitions=num_partitions, replication_factor=replication_factor)
humidity_alerts_topic = NewTopic(name=humidity_alerts, num_partitions=num_partitions, replication_factor=replication_factor)

# Створення нових топіків
try:
    admin_client.create_topics(new_topics=[building_sensors_topic, temperature_alerts_topic, humidity_alerts_topic], validate_only=False)
    print(f"Topic '{building_sensors}' created successfully.")
    print(f"Topic '{temperature_alerts}' created successfully.")
    print(f"Topic '{humidity_alerts}' created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

# Перевіряємо список існуючих топіків
for topic in admin_client.list_topics():
    if my_name in topic:
        print(f"Topic '{topic}' already exists.")

# Закриття зв'язку з клієнтом
admin_client.close()

