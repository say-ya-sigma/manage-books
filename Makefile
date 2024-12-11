up:
	@docker compose up -d

build:
	@docker compose build

down:
	@docker compose down

bash:
	@docker compose exec backend bash

app-chown:
	@sudo chown -R $(USER):$(USER) ./app

docker-chown:
	@sudo chown -R $(USER):$(USER) ./docker

docker-chmod:
	@sudo chmod -R 664 ./docker

install:
	@poetry install

flask-up:
	@poetry run python app/app.py

seed:
	@poetry run python app/seed.py

truncate:
	@poetry run python app/truncate.py

migrate:
	@poetry run alembic upgrade head

generate-migration:
	@poetry run alembic revision --autogenerate -m ${m}

test:
	@poetry run pytest
