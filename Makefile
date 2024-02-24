app-chown:
	@sudo chown -R $(USER):$(USER) ./app

docker-chown:
	@sudo chown -R $(USER):$(USER) ./docker

docker-chmod:
	@sudo chmod -R 664 ./docker

flask-up:
	@poetry run python app/app.py

seed:
	@poetry run python app/seed.py

migrate:
	@poetry run alembic upgrade head
	