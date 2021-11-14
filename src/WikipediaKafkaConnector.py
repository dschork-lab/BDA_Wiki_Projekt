import json
import requests

from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from sseclient import SSEClient
from typing import Dict
from datetime import datetime


def create_producer_instance(bootstrap_server: str) -> KafkaProducer:
    try:
        producer = KafkaProducer(bootstrap_servers=bootstrap_server,
                                 value_serializer=lambda x: json.dumps(x).encode("utf-8"))
    except NoBrokersAvailable:
        print(f"No broker found at {bootstrap_server}")
        raise

    if producer.bootstrap_connected():
        print("connected")
        return producer
    else:
        print("failed to establish connection")
        exit(1)


def check_for_category_response(response, page_id):
    if "categories" not in response["query"]["pages"][f"{page_id}"].keys():
        print(f"{datetime.now()} | response without categories parameter")
        response["query"]["pages"][f"{page_id}"]["categories"] = []
    return response


def merge_event(change_event, old, new) -> Dict[str, str]:
    """
    :param change_event: Change event data
    :param old: Data of the old article version
    :param new: Data of the new article version
    :return: formatted data to send to kafka topic
    """
    try:
        page_id = list(old["query"]["pages"].keys())[0]
        old = check_for_category_response(old, page_id)
        new = check_for_category_response(new, page_id)

        event = {
            "id": change_event['id'],
            "domain": change_event['meta']['domain'],
            "timestamp": change_event['meta']['dt'],
            "revision": {
                "old": change_event['revision']['old'],
                "new": change_event['revision']['new']
            },
            "old_version": {
                "title": old["query"]["pages"][f"{page_id}"]["title"],
                "content": old["query"]["pages"][f"{page_id}"]["extract"],
                "categories": [x["title"][9:] for x in old["query"]["pages"][f"{page_id}"]["categories"]]
            },
            "new_version": {
                "title": new["query"]["pages"][f"{page_id}"]["title"],
                "content": new["query"]["pages"][f"{page_id}"]["extract"],
                "categories": [x["title"][9:] for x in new["query"]["pages"][f"{page_id}"]["categories"]]
            }
        }
        return event
    except KeyError as e:
        print(e)
        pass


if __name__ == "__main__":
    producer = create_producer_instance("localhost:9092")

    event_change_url = 'https://stream.wikimedia.org/v2/stream/recentchange'
    article_information_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts%7Ccategories&meta=&revids={}"

    # Socket for live time changes. Push Query
    for event in SSEClient(event_change_url):
        try:
            event_data = json.loads(event.data)
        except ValueError:
            pass
        else:
            # filter out unwanted change events
            if event_data["type"] == "edit" and event_data["namespace"] == 0:
                if event_data["meta"]["domain"] == "en.wikipedia.org":

                    # request wikipedia article information for the new and old version
                    old_version = requests.get(article_information_url.format(event_data['revision']['old']))
                    new_version = requests.get(article_information_url.format(event_data['revision']['new']))
                    if old_version.status_code == 200 and new_version.status_code == 200:
                        old_version_json = old_version.json()
                        new_version_json = new_version.json()
                        reduced_event = merge_event(event_data, old_version_json, new_version_json)
                        producer.send("article_information", value=reduced_event)
