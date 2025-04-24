build:
	docker build -t custom_celery:latest -f Dockerfile .
rerun:
	docker stop custom_celery
	docker rm custom_celery
	docker run -d --name pcustom_celeryrom -p "8000:8000" custom_celery:latest
run:
	docker run -d --name custom_celery custom_celery:latest
stop:
	docker stop prom
dc_up:
	docker-compose up -d
dc_down:
	docker-compose down
