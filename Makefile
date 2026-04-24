PYTHON ?= python

.PHONY: help install run test db-up db-down migrate seed db-setup db-restart

help:
	@$(PYTHON) scripts/tasks.py help

install:
	@$(PYTHON) scripts/tasks.py install

run:
	@$(PYTHON) scripts/tasks.py run

test:
	@$(PYTHON) scripts/tasks.py test

migrate:
	@$(PYTHON) scripts/tasks.py migrate

seed:
	@$(PYTHON) scripts/tasks.py seed

db-up:
	@$(PYTHON) scripts/tasks.py db-up

db-down:
	@$(PYTHON) scripts/tasks.py db-down

db-setup:
	@$(PYTHON) scripts/tasks.py db-setup

db-restart:
	@$(PYTHON) scripts/tasks.py db-restart
