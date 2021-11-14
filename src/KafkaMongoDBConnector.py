import json
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


# Create Kafka consumer
def create_consumer_instance(bootstrap_server: str, kafka_topic: str) -> KafkaConsumer:
    try:
        consumer = KafkaConsumer(kafka_topic, bootstrap_servers=bootstrap_server)

    except NoBrokersAvailable:
        print(f"No broker found at {bootstrap_server}")
        raise

    if consumer.bootstrap_connected():
        print("connected")
        return consumer
    else:
        print("failed to establish connection")
        exit(1)


# Create MongoDB client to write data into
def create_database_client(mongo_username: str, mongo_password: str, mongo_port: str) -> MongoClient:
    try:
        client = MongoClient(f'mongodb://{mongo_username}:{mongo_password}@localhost:{mongo_port}/')
        client.server_info()
        return client
    except ServerSelectionTimeoutError as err:
        print(err)


if __name__ == "__main__":
    bootstrap_server = 'localhost:9092'
    kafka_topic = 'article_information'
    consumer = create_consumer_instance(bootstrap_server, kafka_topic)

    mongo_username = 'root'
    mongo_password = 'example'
    mongo_port = '27017'
    client = create_database_client(mongo_username, mongo_password, mongo_port)

    # get database from MongoDB client and add collections for changes and pre-aggregated mood
    article_information_db = client.article_information
    changes_collection = article_information_db.changes
    id_mood_collection = article_information_db.id_mood

    # for every message from consumer put data into database
    for msg in consumer:
        msg_json = json.loads(msg.value)
        changes_collection.insert_one(msg_json)

        # ToDo: Implement mood analysis
        msg_mood = {
            'id': msg_json['id'],
            'old_revision': msg_json['revision']['old'],
            'new_revision': msg_json['revision']['new'],
            'old_mood': '1',
            'new_mood': '2'
        }
        id_mood_collection.insert_one(msg_mood)
