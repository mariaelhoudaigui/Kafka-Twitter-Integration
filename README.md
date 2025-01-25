
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
### 1. **Install Kafka**:
   Ensure that you have **Apache Kafka** installed and running on your local machine or a remote server. 

### 2. **Twitter Developer Account**:
   - To use the Twitter API, you will need to create a Twitter Developer account and generate the necessary credentials (API keys).
   - After creating an account, create an app and retrieve your **API Key**, **API Secret**, **Access Token**, **Access Secret**, and **Bearer Token**.

### 3. **Install MySQL**:
   - Install MySQL and create a database (`kafka-project`) with a table for storing tweets.

## Requirements:
Install the following Python libraries to run the application:
```
pip install confluent_kafka mysql-connector-python tweepy
```
