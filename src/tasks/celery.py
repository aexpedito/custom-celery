
from celery import Celery
from kafka import KafkaConsumer
import json

app = Celery('tasks', broker='amqp://admin:mypass@celery-broker:5672', include=['tasks'])

#Optional configuration
app.conf.update(
    result_expires = 3600,
)

consumer = KafkaConsumer(
	'test_topic',
	bootstrap_servers='kafka:9093',
	group_id='celery',
	max_poll_records= 1,
	#value_deserializer=lambda m: json.loads(m.decode('utf-8')),
	auto_offset_reset='latest'
)

#TODO Pegar a mensagem do kafka
#TODO adicionar logging para o celery
if __name__ == '__main__':

    # Cria kafka consumer

    # Inicializa o Celery app
    print("Celery worker started.")
    app.start()

    # Para cada mensagem do topico Kafka
    # for message in consumer:
    # app.add.delay(message.value)

    print("Starting consumer...")
    #for message in consumer:
    #    print(json.loads(message.value))
