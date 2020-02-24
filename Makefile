install:
	pip install --upgrade .

install-dev:
	pip install --upgrade -e .

install-build-tools:
	pip install grpcio-tools grpclib

BUILD_TARGET=pytrtis/gen
SED=sed -i -E 's/import (.+)_pb2/from pytrtis.gen import \1_pb2/g'

build-proto:
	python -m grpc_tools.protoc -Iproto\
		--python_out=$(BUILD_TARGET)\
		--grpc_python_out=$(BUILD_TARGET)\
		--python_grpc_out=$(BUILD_TARGET)\
		proto/*.proto


	$(SED) pytrtis/gen/grpc_service_grpc.py
	$(SED) pytrtis/gen/grpc_service_pb2_grpc.py
	$(SED) pytrtis/gen/grpc_service_pb2.py

	$(SED) pytrtis/gen/grpc_service_v2_grpc.py
	$(SED) pytrtis/gen/grpc_service_v2_pb2_grpc.py
	$(SED) pytrtis/gen/grpc_service_v2_pb2.py

	$(SED) pytrtis/gen/server_status_pb2.py
