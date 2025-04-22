build:
	docker build -t custom_celery:latest -f Dockerfile .
rerun:
	docker stop prom
	docker rm prom
	docker run -d --name prom -p "8000:8000" prom-flask:latest
run:
	docker run -d --name custom_celery custom_celery:latest
stop:
	docker stop prom
dc_up:
	docker-compose up -d
dc_down:
	docker-compose down
