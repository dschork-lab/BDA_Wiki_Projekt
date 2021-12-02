import json
import re
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from MoodAnalysis import check_mood

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

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

        # Remove HTML-Tags
        msg_json['old_version']['content'] = re.sub(CLEANR, '', msg_json['old_version']['content'])
        msg_json['new_version']['content'] = re.sub(CLEANR, '', msg_json['new_version']['content'])

        # Save full change entry in Database
        changes_collection.insert_one(msg_json)

        # Mood analysis for the content of the old and new version
        oldVersionMood = check_mood(msg_json['old_version']['content'])
        newVersionMood = check_mood(msg_json['new_version']['content'])
        msg_mood = {
            'id': msg_json['id'],
            'old_revision': msg_json['old_revision'],
            'new_revision': msg_json['new_revision'],
            'old_positive': oldVersionMood[0],
            'old_negative': oldVersionMood[1],
            'old_anger': oldVersionMood[2],
            'old_anticipation': oldVersionMood[3],
            'old_disgust': oldVersionMood[4],
            'old_fear': oldVersionMood[5],
            'old_joy': oldVersionMood[6],
            'old_sadness': oldVersionMood[7],
            'old_surprise': oldVersionMood[8],
            'old_trust': oldVersionMood[9],
            'new_positive': newVersionMood[0],
            'new_negative': newVersionMood[1],
            'new_anger': newVersionMood[2],
            'new_anticipation': newVersionMood[3],
            'new_disgust': newVersionMood[4],
            'new_fear': newVersionMood[5],
            'new_joy': newVersionMood[6],
            'new_sadness': newVersionMood[7],
            'new_surprise': newVersionMood[8],
            'new_trust': newVersionMood[9],
            'old_content_length': len(msg_json['old_version']['content'].split()),
            'new_content_length': len(msg_json['new_version']['content'].split())
        }

        # Save aggregated mood analysis in database
        id_mood_collection.insert_one(msg_mood)
