init:
	cp .env.dev .env
	docker-compose build --no-cache
	docker-compose up -d

up:
	docker-compose up -d

down:
	docker-compose down

sh:
	docker-compose exec uwsgi bash
