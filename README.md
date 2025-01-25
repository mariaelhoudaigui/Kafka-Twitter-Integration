
## Description
This project demonstrates how to integrate **Twitter API** with **Apache Kafka** for real-time streaming of tweets. 
The application uses the Twitter API to fetch recent tweets based on specified keywords and sends these tweets as messages to a Kafka topic. 
A Kafka consumer then reads the messages from the topic and stores them in a **MySQL** database for further analysis.

### Key Features:
- **Twitter API Integration**: Fetches real-time tweets containing specific keywords from Twitter.
- **Kafka Producer**: Sends tweets to a Kafka topic in real-time.
- **Kafka Consumer**: Reads tweets from the Kafka topic and stores them in a MySQL database.
- **MySQL Integration**: Stores the tweet data in a relational database for easy querying and analysis.

## Technologies Used:
- **Kafka**: For streamlining the real-time data flow between the producer and consumer.
- **Twitter API**: To fetch live tweets for processing.
- **MySQL**: For storing tweet data.
- **Python**: Programming language for implementing Kafka Producers, Consumers, and interacting with the Twitter API.
- **Confluent Kafka Python Client**: To interact with Kafka's messaging system.
- **Tweepy**: A Python library for interacting with the Twitter API.

## Prerequisites:
### 1. **Install Apache Kafka:**
   Apache Kafka is a distributed event streaming platform. Before starting, ensure that you have Kafka installed on your local machine or on a server. Follow these steps:

   - **Download Kafka**: Go to the [official Kafka website](https://kafka.apache.org/downloads) and download the appropriate version.
   - **Extract Kafka**: Unzip the downloaded file and move it to your desired directory.
   - **Install Java**: Kafka requires Java to run. If Java is not installed, download and install it from [Oracle's website](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html)

### 2.   **Start Zookeeper and Kafka:**
   Kafka requires **Zookeeper** for coordination. You need to start Zookeeper and then Kafka:
   - Open a terminal and navigate to the Kafka directory.
   - **Start Zookeeper** (in one terminal window):
     ```bash
     bin/zookeeper-server-start.sh config/zookeeper.properties
     ```
   - **Start Kafka** (in another terminal window):
     ```bash
     bin/kafka-server-start.sh config/server.properties
     ```

### 3. **Create a Kafka Topic:**
   After starting Kafka, create a Kafka topic to which the producer will send tweets:
   ```bash
   bin/kafka-topics.sh --create --topic twitter-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
 ```

### 4.Install MySQL:
You need to install MySQL and set up a database to store the tweet data.

### 5.Running the Application:

- **Running the Kafka Producer (producer.py):**
This script fetches recent tweets containing the specified keywords from Twitter and sends them to the Kafka topic.

```bash
python producer.py
```
- **Running the Kafka Consumer (consumer.py):**
The Kafka consumer script will read the tweets from the Kafka topic and store them in the MySQL database.
```bash
python consumer.py
```
## Requirements:
Install the following Python libraries to run the application:
```
pip install confluent_kafka mysql-connector-python tweepy
```
