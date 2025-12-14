# Makefile for testpython project

.PHONY: help install test clean build run format lint

help:
	@echo "Available commands:"
	@echo "  make install    - Install package and dependencies"
	@echo "  make test       - Run tests"
	@echo "  make run        - Run the main application"
	@echo "  make format     - Format code with black"
	@echo "  make lint       - Run code linters"
	@echo "  make clean      - Remove build artifacts"
	@echo "  make build      - Build the package"

install:
	pip install -e ".[dev]"

test:
	python -m unittest discover tests -v

run:
	python -m testpython.main

format:
	black testpython tests

lint:
	flake8 testpython tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

build:
	python setup.py sdist bdist_wheel
