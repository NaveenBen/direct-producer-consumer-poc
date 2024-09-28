from dotenv import load_dotenv
import os
import pika
import argparse
import time
import random
load_dotenv()

rabbitmq_uri = os.getenv('RABBITMQ_URI')
print(rabbitmq_uri)

connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))

channel = connection.channel()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    time.sleep(round(random.uniform(0, 1),1))
    print(" [x] Done")
    
    
channel.exchange_declare(exchange='test', exchange_type='direct', durable=True)
channel.queue_declare(queue='test', durable=True)
channel.queue_bind(exchange='test', queue='test', routing_key='test')

channel.basic_consume(queue='test', on_message_callback=callback,auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
