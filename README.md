# BDA_Wiki_Projekt
Big Data Analytics Projekt



# Quick start

### Prerequisites:
- Git
- Docker  

Download the repository and navigate to the docker folder.

```shell script
git clone https://github.com/dschork-lab/BDA_Wiki_Projekt && cd BDA_Wiki_Projekt/docker
```

Then start the docker containers via docker compose

```shell script
docker compose up -d
```

Once all the images are downloaded and the containers are started you can access the broker via

```shell script
docker exec -it broker bash
```



### Creating  
```shell script
kafka-topics --create --topic example_topic --zookeeper zookeeper:2181 --partitions 1 --replication-factor 1
```

### Consumer
```shell script
kafka-console-consumer --topic example_topic --bootstrap-server broker:29092 --from-beginning
```

### Producer
```shell script
kafka-console-producer --broker-list broker:29092 --topic example_topic
```
---


Alternatively creating the topics can be done via the UI-Component

Access ``localhost:9000`` and click `+ new` 

---
##Vor Nutzung der Wikipedia Producer Python Datei zu beachten: 

###Zuvor zu installierende Python Dateien:
```shell script
pip install kafka-python
pip install pymongo
pip install requests
```
---

##Wikipedia Guide
### Wikipedia Topic anlegen
```shell script
kafka-topics --create --topic article_information --zookeeper zookeeper:2181 --partitions 1 --replication-factor 1
```

### Consumer & Producer
Python-Dateien ``KafkaMongoDBConnector.py`` und ``WikipediaKafakaConnector.py`` ausführen

### MongoDB Web Interface
Access via ``localhost:8081``
