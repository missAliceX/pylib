test:
	coverage run -m pytest
	coverage report -m *.py pylib/**/*.py

install:
	pip-upgrade *.txt
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

generate:
	python -m grpc_tools.protoc -I proto \
		--python_out=pylib/proto --grpc_python_out=pylib/proto \
		proto/*.proto
	2to3 -wn -f import pylib/proto/*.py
