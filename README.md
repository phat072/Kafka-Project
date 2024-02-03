# Data ingestion using kafka

## My version
    - Python ^3.11
    - Docker version 25.0.0, build e758fe5

## Introduction

The first step in almost every data project is data ingestion. 
Regardless of the data's location or format, you must find a way to 
transform it into an incoming data flow for your project. This allows 
you to clean, process, and ultimately generate insights or build 
machine-learning models from it.

In this project, we aim to build and connect the necessary components 
for a data ingestion setup using Kafka and Python. For the sake of 
simplicity, we will be using a *'.csv'* file as the data source and 
simulate a continuous incoming data flow with its data. Think of it as 
something similar to a temperature sensor or stock prices during open 
hours. 

You can check the Medium article for this project in: [A Python Kafka Producer](https://bit.ly/python-kafka-producer)

## Quickstart

Create and active your virtual environment.

    - Run env 
        + python3 -m venv venv
        + source venv/bin/activate
    - Poetry option:
        + ```poetry install```
    - Pip option:
        + I have created a `requirements.txt` from the `pyproject.toml` file. Due to this, you can install dependencies using pip.
        ```pip install -r requirements.txt```

The first thing you need to do is start a *Server* (a *Server* is a server which has Kafka running on it). For this, we are going to use a `docker-compose.yaml` file to set up the *Server* service.


```bash
docker compose up -d
```

Now that we have a the Kafka *server* running, we need to tell it how to organize the incomming data. For this, the *server* organizes and store the incomming messages (events) in *topics*. *"Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder".* Let's tell the server where to put all this incomming data:

Now that we have the Kafka Server up and running, it's time to let it know how to handle all the incoming data. Basically, the *Server* organizes and stores those incoming messages (which we'll call events) into topics. Think of topics like folders in a file system, and the events are like the files inside those folders. So, let's tell the server where to put all this incoming data:

1. Open an interective terminal in the *Server* container:
```bash
docker exec -it server bash
```

2. Then, navigate to the following directory`/opt/bitnami/kafka/bin`:
```bash
cd opt/bitnami/kafka/bin
```

3. Create a topic:

Let's create our first topic:
```bash
./kafka-topics.sh --create --bootstrap-server kafka-server:9092 --replication-factor 1 --partitions 1 --topic room_1
```

