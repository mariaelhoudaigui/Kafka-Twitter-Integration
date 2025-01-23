import json
import tweepy
from confluent_kafka import Producer

# Clés API Twitter
API_KEY = ""
API_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
BEARER_TOKEN = ""

# Configuration du producteur Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'twitter-producer'
}
producer = Producer(conf)

# Fonction de callback pour la livraison du message Kafka
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Authentification avec l'API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Fonction pour rechercher des tweets
def fetch_tweets(keywords):
    try:
        query = f"{keywords} lang:en"
        for tweet in client.search_recent_tweets(query=query, tweet_fields=["created_at", "text", "author_id"], max_results=10).data:
            tweet_data = json.dumps({
                "id": tweet.id,
                "text": tweet.text,
                "created_at": tweet.created_at.isoformat(),
                "author_id": tweet.author_id
            })
            producer.produce('twitter-topic', tweet_data.encode('utf-8'), callback=delivery_report)
            producer.flush()
    except Exception as e:
        print(f"Error fetching tweets: {e}")

# Rechercher des tweets contenant certains mots-clés
fetch_tweets("Kafka OR Python")


