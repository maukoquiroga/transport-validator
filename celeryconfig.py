import os

broker_url = os.environ.get('RABBITMQ_URL') or 'amqp://localhost'
result_backend = os.environ.get('MONGODB_URL') or 'mongodb'
