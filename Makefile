PYTHON ?= python

.PHONY: help install run test

help:
	@$(PYTHON) scripts/tasks.py help

install:
	@$(PYTHON) scripts/tasks.py install

run:
	@$(PYTHON) scripts/tasks.py run

test:
	@$(PYTHON) scripts/tasks.py test
