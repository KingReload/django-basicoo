.PHONY: all clean install frontend lint eslint isort flake8 exampledata docs requirements


all: clean install frontend compilemessages exampledata

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' -delete
	rm -rf basicoo/static/*.{css,js,map}
	rm -rf basicoo/static/{images,sourcemaps}

install:
	pip3 install -r requirements.txt

frontend:
	yarn install && yarn run compile

watch:
	yarn start

exampledata:
	./manage.py migrate
	./manage.py loaddata exampledata/users.json

docs:
	$(MAKE) -C docs html


requirements:
	pip3 install pip-tools
	pip-compile


#
# Utility
makemessages:
	cd basicoo && DJANGO_SETTINGS_MODULE=basicoo.settings python3 ../../manage.py makemessages -all
	cd frontend && DJANGO_SETTINGS_MODULE=basicoo.settings python3 ../manage.py makemessages -d djangojs -all

compilemessages:
	cd basicoo  && DJANGO_SETTINGS_MODULE=basicoo.settings python ../../manage.py compilemessages

#
# Testing
#
test:
	yarn test
	py.test --nomigrations --reuse-db --ignore=tests/functional tests/

retest:
	yarn test
	py.test --nomigrations --reuse-db --lf --ignore=tests/functional tests/

coverage:
	py.test --nomigrations --ignore=tests/functional --reuse-db tests/ --cov=basicoo --cov-report=term-missing



#
# Lint targets
#
lint: flake8 isort eslint

eslint:
	./node_modules/.bin/eslint frontend/**/*.js

isort:
	pip install isort
	isort --recursive --check-only --diff src tests

flake8:
	pip3 install flake8 flake8-debugger flake8-blind-except flake8-imports
	flake8 basicoo/ --ignore=W191  #tests/
