from dotenv import load_dotenv
import os
import pika
import argparse
import time

load_dotenv()

rabbitmq_uri = os.getenv('RABBITMQ_URI')
print(rabbitmq_uri)

# Connect to RabbitMQ

connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))

# Do something with the connection
channel = connection.channel()


channel.exchange_declare(exchange='test', exchange_type='direct',durable=True)
channel.queue_declare(queue='test', durable=True)
channel.queue_bind(exchange='test', queue='test', routing_key='test')
x=0
while True:
    message = f"Hello World! {x}"
    channel.basic_publish(exchange='test', routing_key='test', body=message)
    print(f" [x] Sent {message}")
    x+=1
    
