from celery import Celery

app = Celery('tasks', broker='amqp://admin:mypass@celery-broker:5672', include=['tasks'])

#Optional configuration
app.conf.update(
    result_expires = 3600,
)

# Pegar a mensagem do 
if __name__ == '__main__':

    # Cria kafka consumer

    # Inicializa o Celery app
    app.start()

    # Para cada mensagem do topico Kafka
    # for message in consumer:
    # app.add.delay(message.value)
    print("Celery worker started.")
