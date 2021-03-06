import json
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from datetime import datetime
from MoodAnalysis import check_mood


# Create Kafka consumer
def create_consumer_instance(bootstrap_server: str, kafka_topic: str, group_id: str) -> KafkaConsumer:
    try:
        consumer = KafkaConsumer(kafka_topic, group_id=group_id, bootstrap_servers=bootstrap_server)

    except NoBrokersAvailable:
        print(f"FATAL | {datetime.now()} | No broker found at {bootstrap_server}")
        raise

    if consumer.bootstrap_connected():
        print(f"INFO | {datetime.now()} | To kafka broker connected")
        return consumer

    else:
        print(f"FATAL | {datetime.now()} | Failed to establish connection to broker")
        exit(1)


# Create MongoDB client to write data into
def create_database_client(mongo_username: str, mongo_password: str, mongo_port: str) -> MongoClient:
    try:
        client = MongoClient(f'mongodb://{mongo_username}:{mongo_password}@localhost:{mongo_port}/')
        client.server_info()
        print(f"INFO | {datetime.now()} | To database connected")
        return client
    except ServerSelectionTimeoutError as error_message:
        print("FATAL | {datetime.now()} | Failed to establish connection to database")
        print(error_message)
        exit(1)


if __name__ == "__main__":
    bootstrap_server = 'localhost:9092'
    kafka_topic = 'article_information'
    kafka_consumer_group = "mood-analysis-group-1"
    consumer = create_consumer_instance(bootstrap_server, kafka_topic, kafka_consumer_group)

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

        # Save full change entry in Database
        changes_collection.insert_one(msg_json)
        print(f"INFO | {datetime.now()} | Send new change event to database")

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
        print(f"INFO | {datetime.now()} | Send new analysed change event to database")
