python = venv/bin/python
pip = venv/bin/pip
pytest = venv/bin/pytest

up:
	docker compose up

pull:
	docker compose pull

down:
	docker compose down

run-http-server:
	$(python) run_http_server.py

uninstall-unrequired-libraries:
	$(pip) freeze | grep -v -f requirements.txt - | grep -v '^#' | xargs $(pip) uninstall -y || echo "OK, you dont have any unrequired libraries"

install: uninstall-unrequired-libraries
	$(pip) install -r requirements.txt

install-venv:
	python -m virtualenv venv --python python3

update-requirements:
	$(pip) freeze > requirements.txt

test: clean
	$(pytest) -vvvv tests

coverage:
	$(pytest) -vvvv --cov src --cov-report term-missing

clean-logs:
	rm -f logs/*.log
	rm -f logs/*.log.jsonl

clean-test-reports:
	mkdir -p test_reports
	rm -f test_reports/*.xml

clean: clean-logs clean-test-reports