from celery import Celery

app = Celery('tasks', broker='amqp://admin:mypass@celery-broker:5672', include=['tasks'])

#Optional configuration
app.conf.update(
    result_expires = 3600,
)

if __name__ == '__main__':
    app.start()
