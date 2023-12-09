create-env:
	@pip3 install virtualenv && \
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate &&\
	pip install --upgrade pip &&\
	python3 -m pip install -r src/core/requirements.txt &&\
	python3 -m pip install -r src/desktop/requirements.txt

install-tools:
	@brew install python-tk

test:
	@pytest --cov=src tests/

run-desktop:
	@python3 src/desktop/main.py

package-desktop:
	@scripts/release.sh
