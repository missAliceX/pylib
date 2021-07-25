install:
	pip-upgrade
	pip install -U -r requirements.txt
	pip install -U -r requirements.dev.txt

generate:
	python -m grpc_tools.protoc -I proto \
		--python_out=src/pylib/proto --grpc_python_out=src/pylib/proto \
		proto/*.proto