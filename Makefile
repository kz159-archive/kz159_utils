test:
	pytest .

dev:
	pip3 install requirements-dev.txt

dep:
	pip3 install requirements.txt

pre-commit:
	pre-commit run --all-files
