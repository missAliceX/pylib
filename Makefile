.EXPORT_ALL_VARIABLES:

POSTGRES_HOST=localhost
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=maindb

install:
	pip-upgrade
	pip install -U -r requirements.txt

generate:
	python -m grpc_tools.protoc -I proto \
		--python_out=pylib/proto --grpc_python_out=pylib/proto \
		proto/*.proto
	2to3 -wn -f import pylib/proto/*.py
