create-env:
	@pip3 install virtualenv && \
	python3 -m venv ./.venv && \
	source ./.venv/bin/activate &&\
	python3 -m pip install -r requirements.txt

install-tk:
	@brew install python-tk

test:
	@pytest --cov=hax tests/

run:
	@python3 src/main.py

package:
	@scripts/release.sh
