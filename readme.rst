=================
SCRAPPERHUB PROJECT
=================
-------------------------
FREE and open source project
-------------------------

Introduction
============

SCRAPPERHUB is free, open source middleware / standalone app that provides all scraping features. Extended with fully integrated GUI and API can be easliy adapted to your stack.

Usefull info:
----------

1. Endpoints:
  - GraphQL API endpoint: {domain}/graphql/
  - Django admin: {domain}/admin/
  - Base app addres: {domain}/
  
2. SuperUser credentials:
  - login: supervisor@supervisor.pl
  - password: TsQ@GmQhuXp72cp8

3. User credentials:
  - login: user@user.pl
  - password: ZsA!smYtuXp77dc1

4. Code coverage
  - Currently 90%

Usefull comands:
----------

1. Tests:
  - Execute test: python manage.py test --settings=scrapper.settings_local
  - Coverage: coverage run manage.py test --settings=scrapper.settings_local
  - Coverage raport: coverage report
  
2. Mock data:
  - Load: python manage.py loaddata mock_data.yaml

3. Run Application:
  - via docker: docker-compose up
  - via local: python manage.py runserver
  
4. Code maintenance:
  - black: black .
  - isort: isort .
  - flake: flake8.
  