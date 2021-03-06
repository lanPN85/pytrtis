# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pytrtis.gen import grpc_service_pb2 as grpc__service__pb2


class GRPCServiceStub(object):
  """@@
  @@.. cpp:var:: service GRPCService
  @@
  @@   Inference Server GRPC endpoints.
  @@
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Status = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCService/Status',
        request_serializer=grpc__service__pb2.StatusRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.StatusResponse.FromString,
        )
    self.Health = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCService/Health',
        request_serializer=grpc__service__pb2.HealthRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.HealthResponse.FromString,
        )
    self.Infer = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCService/Infer',
        request_serializer=grpc__service__pb2.InferRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.InferResponse.FromString,
        )
    self.StreamInfer = channel.stream_stream(
        '/nvidia.inferenceserver.GRPCService/StreamInfer',
        request_serializer=grpc__service__pb2.InferRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.InferResponse.FromString,
        )
    self.ModelControl = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCService/ModelControl',
        request_serializer=grpc__service__pb2.ModelControlRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.ModelControlResponse.FromString,
        )
    self.SharedMemoryControl = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCService/SharedMemoryControl',
        request_serializer=grpc__service__pb2.SharedMemoryControlRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.SharedMemoryControlResponse.FromString,
        )
    self.Repository = channel.unary_unary(
        '/nvidia.inferenceserver.GRPCService/Repository',
        request_serializer=grpc__service__pb2.RepositoryRequest.SerializeToString,
        response_deserializer=grpc__service__pb2.RepositoryResponse.FromString,
        )


class GRPCServiceServicer(object):
  """@@
  @@.. cpp:var:: service GRPCService
  @@
  @@   Inference Server GRPC endpoints.
  @@
  """

  def Status(self, request, context):
    """@@  .. cpp:var:: rpc Status(StatusRequest) returns (StatusResponse)
    @@
    @@     Get status for entire inference server or for a specified model.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Health(self, request, context):
    """@@  .. cpp:var:: rpc Health(HealthRequest) returns (HealthResponse)
    @@
    @@     Check liveness and readiness of the inference server.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Infer(self, request, context):
    """@@  .. cpp:var:: rpc Infer(InferRequest) returns (InferResponse)
    @@
    @@     Request inference using a specific model. [ To handle large input
    @@     tensors likely need to set the maximum message size to that they
    @@     can be transmitted in one pass.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamInfer(self, request_iterator, context):
    """@@  .. cpp:var:: rpc StreamInfer(stream InferRequest) returns (stream
    @@     InferResponse)
    @@
    @@     Request inferences using a specific model in a streaming manner.
    @@     Individual inference requests sent through the same stream will be
    @@     processed in order and be returned on completion
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModelControl(self, request, context):
    """@@  .. cpp:var:: rpc ModelControl(ModelControlRequest) returns
    @@     (ModelControlResponse)
    @@
    @@     Request to load / unload a specified model.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SharedMemoryControl(self, request, context):
    """@@  .. cpp:var:: rpc SharedMemoryControl(SharedMemoryControlRequest) returns
    @@     (SharedMemoryControlResponse)
    @@
    @@     Request to register / unregister a specified shared memory region.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Repository(self, request, context):
    """@@  .. cpp:var:: rpc Status(RepositoryRequest) returns (RepositoryResponse)
    @@
    @@     Get status associated with the model repository.
    @@
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GRPCServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Status': grpc.unary_unary_rpc_method_handler(
          servicer.Status,
          request_deserializer=grpc__service__pb2.StatusRequest.FromString,
          response_serializer=grpc__service__pb2.StatusResponse.SerializeToString,
      ),
      'Health': grpc.unary_unary_rpc_method_handler(
          servicer.Health,
          request_deserializer=grpc__service__pb2.HealthRequest.FromString,
          response_serializer=grpc__service__pb2.HealthResponse.SerializeToString,
      ),
      'Infer': grpc.unary_unary_rpc_method_handler(
          servicer.Infer,
          request_deserializer=grpc__service__pb2.InferRequest.FromString,
          response_serializer=grpc__service__pb2.InferResponse.SerializeToString,
      ),
      'StreamInfer': grpc.stream_stream_rpc_method_handler(
          servicer.StreamInfer,
          request_deserializer=grpc__service__pb2.InferRequest.FromString,
          response_serializer=grpc__service__pb2.InferResponse.SerializeToString,
      ),
      'ModelControl': grpc.unary_unary_rpc_method_handler(
          servicer.ModelControl,
          request_deserializer=grpc__service__pb2.ModelControlRequest.FromString,
          response_serializer=grpc__service__pb2.ModelControlResponse.SerializeToString,
      ),
      'SharedMemoryControl': grpc.unary_unary_rpc_method_handler(
          servicer.SharedMemoryControl,
          request_deserializer=grpc__service__pb2.SharedMemoryControlRequest.FromString,
          response_serializer=grpc__service__pb2.SharedMemoryControlResponse.SerializeToString,
      ),
      'Repository': grpc.unary_unary_rpc_method_handler(
          servicer.Repository,
          request_deserializer=grpc__service__pb2.RepositoryRequest.FromString,
          response_serializer=grpc__service__pb2.RepositoryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'nvidia.inferenceserver.GRPCService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
