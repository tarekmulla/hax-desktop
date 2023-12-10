lint:
	@poetry run ./scripts/linting_check.sh

test:
	@poetry run pytest

install-tools:
	@brew install python-tk

run-desktop:
	@poetry run python haxdesktop/main.py

package-desktop:
	@scripts/release.sh
