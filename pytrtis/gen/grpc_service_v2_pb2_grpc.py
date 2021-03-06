# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pytrtis.gen import grpc_service_v2_pb2 as grpc__service__v2__pb2


class GRPCInferenceServiceStub(object):
  """@@
  @@.. cpp:var:: service InferenceService
  @@
  @@   Inference Server GRPC endpoints.
  @@
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ServerLive = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ServerLive',
        request_serializer=grpc__service__v2__pb2.ServerLiveRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ServerLiveResponse.FromString,
        )
    self.ServerReady = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ServerReady',
        request_serializer=grpc__service__v2__pb2.ServerReadyRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ServerReadyResponse.FromString,
        )
    self.ModelReady = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ModelReady',
        request_serializer=grpc__service__v2__pb2.ModelReadyRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ModelReadyResponse.FromString,
        )
    self.ServerMetadata = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ServerMetadata',
        request_serializer=grpc__service__v2__pb2.ServerMetadataRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ServerMetadataResponse.FromString,
        )
    self.ModelMetadata = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ModelMetadata',
        request_serializer=grpc__service__v2__pb2.ModelMetadataRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ModelMetadataResponse.FromString,
        )
    self.ModelInfer = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ModelInfer',
        request_serializer=grpc__service__v2__pb2.ModelInferRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ModelInferResponse.FromString,
        )
    self.ModelConfig = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCInferenceService/ModelConfig',
        request_serializer=grpc__service__v2__pb2.ModelConfigRequest.SerializeToString,
        response_deserializer=grpc__service__v2__pb2.ModelConfigResponse.FromString,
        )


class GRPCInferenceServiceServicer(object):
  """@@
  @@.. cpp:var:: service InferenceService
  @@
  @@   Inference Server GRPC endpoints.
  @@
  """

  def ServerLive(self, request, context):
    """@@  .. cpp:var:: rpc ServerLive(ServerLiveRequest) returns
    @@       (ServerLiveResponse)
    @@
    @@     Check liveness of the inference server.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerReady(self, request, context):
    """@@  .. cpp:var:: rpc ServerReady(ServerReadyRequest) returns
    @@       (ServerReadyResponse)
    @@
    @@     Check readiness of the inference server.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelReady(self, request, context):
    """@@  .. cpp:var:: rpc ModelReady(ModelReadyRequest) returns
    @@       (ModelReadyResponse)
    @@
    @@     Check readiness of a model in the inference server.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ServerMetadata(self, request, context):
    """@@  .. cpp:var:: rpc ServerMetadata(ServerMetadataRequest) returns
    @@       (ServerMetadataResponse)
    @@
    @@     Get server metadata.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelMetadata(self, request, context):
    """@@  .. cpp:var:: rpc ModelMetadata(ModelMetadataRequest) returns
    @@       (ModelMetadataResponse)
    @@
    @@     Get model metadata.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelInfer(self, request, context):
    """@@  .. cpp:var:: rpc ModelInfer(ModelInferRequest) returns
    @@       (ModelInferResponse)
    @@
    @@     Perform inference using a specific model.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelConfig(self, request, context):
    """@@  .. cpp:var:: rpc ModelConfig(ModelConfigRequest) returns
    @@       (ModelConfigResponse)
    @@
    @@     Get model configuration.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GRPCInferenceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ServerLive': grpc.unary_unary_rpc_method_handler(
          servicer.ServerLive,
          request_deserializer=grpc__service__v2__pb2.ServerLiveRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ServerLiveResponse.SerializeToString,
      ),
      'ServerReady': grpc.unary_unary_rpc_method_handler(
          servicer.ServerReady,
          request_deserializer=grpc__service__v2__pb2.ServerReadyRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ServerReadyResponse.SerializeToString,
      ),
      'ModelReady': grpc.unary_unary_rpc_method_handler(
          servicer.ModelReady,
          request_deserializer=grpc__service__v2__pb2.ModelReadyRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ModelReadyResponse.SerializeToString,
      ),
      'ServerMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.ServerMetadata,
          request_deserializer=grpc__service__v2__pb2.ServerMetadataRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ServerMetadataResponse.SerializeToString,
      ),
      'ModelMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.ModelMetadata,
          request_deserializer=grpc__service__v2__pb2.ModelMetadataRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ModelMetadataResponse.SerializeToString,
      ),
      'ModelInfer': grpc.unary_unary_rpc_method_handler(
          servicer.ModelInfer,
          request_deserializer=grpc__service__v2__pb2.ModelInferRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ModelInferResponse.SerializeToString,
      ),
      'ModelConfig': grpc.unary_unary_rpc_method_handler(
          servicer.ModelConfig,
          request_deserializer=grpc__service__v2__pb2.ModelConfigRequest.FromString,
          response_serializer=grpc__service__v2__pb2.ModelConfigResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nvidia.inferenceserver.GRPCInferenceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
