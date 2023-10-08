create-env:
	@pip3 install virtualenv && \
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate &&\
	python3 -m pip install -r requirements.txt

install-tools:
	@brew install python-tk && \
	brew install hashcat

test:
	@pytest --cov=src tests/

run:
	@python3 src/main.py

package:
	@scripts/release.sh
