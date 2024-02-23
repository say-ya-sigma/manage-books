bash:
	@docker compose exec backend bash

poetory-install:
	@docker compose exec backend poetry install --no-root

poetory-lock:
	@docker compose exec backend poetry lock

app-chown:
	@sudo chown -R $(USER):$(USER) ./app

flask-up:
	@poetry run python app/app.py
	