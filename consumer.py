from confluent_kafka import Consumer, KafkaException, KafkaError
import mysql.connector
import json  # Pour parser le message JSON

# Configurations Kafka
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)
topic = 'twitter-topic'
consumer.subscribe([topic])

# Connexion à MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'kafka-project'
}
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

try:
    while True:
        # Récupérer un message depuis Kafka
        msg = consumer.poll(1.0)

        if msg is None:
            continue  # Aucun message pour l'instant
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"Fin de la partition {msg.topic()} [{msg.partition()}] offset {msg.offset()}")
                continue
            else:
                print(f"Erreur Kafka : {msg.error()}")
                raise KafkaException(msg.error())

        # Décoder et parser le message
        message_content = msg.value().decode('utf-8')
        message_json = json.loads(message_content)  # Assurez-vous que le message Kafka est au format JSON

        # Extraire les données nécessaires
        message_id = message_json.get('id')
        message_text = message_json.get('text')
        message_created_at = message_json.get('created_at')
        message_author_id = message_json.get('author_id')

        # Insérer dans la table tweets
        cursor.execute(
            "INSERT INTO tweets (id, text, created_at, author_id) VALUES (%s, %s, %s, %s)",
            (message_id, message_text, message_created_at, message_author_id)
        )
        conn.commit()  # Valider l'insertion
        print(f"Message inséré dans MySQL : {message_content}")

except KeyboardInterrupt:
    print("Arrêt par l'utilisateur.")
finally:
    # Fermeture des ressources
    consumer.close()
    cursor.close()
    conn.close()
    print("Consommateur Kafka et connexion MySQL fermés.")

