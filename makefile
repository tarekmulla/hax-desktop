lint:
	@poetry run ./scripts/linting_check.sh

test:
	@poetry run pytest

lock:
	@poetry lock &&\
	poetry install &&\
	poetry lock

install-tools:
	@brew install python-tk

run:
	@poetry run python haxdesktop/main.py

release:
	@scripts/release.sh
