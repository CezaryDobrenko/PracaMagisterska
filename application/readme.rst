RUN TESTS:
python manage.py test --settings=scrapper.settings_local

RUN COVERAGE:
coverage erase 
coverage run manage.py test --settings=scrapper.settings_local
coverage report