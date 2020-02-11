init:
	cp ./api/config.py.dev ./api/config.py
	docker-compose build --no-cache
	docker-compose up -d

up:
	docker-compose up -d

down:
	docker-compose down

sh:
	docker-compose exec uwsgi bash

ps:
	docker-compose ps
