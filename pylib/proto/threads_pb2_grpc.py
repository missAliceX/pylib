# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import threads_pb2 as threads__pb2


class ThreadsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProjectThreads = channel.unary_unary(
                '/ThreadsService/GetProjectThreads',
                request_serializer=threads__pb2.GetProjectThreadsRequest.SerializeToString,
                response_deserializer=threads__pb2.GetProjectThreadsResponse.FromString,
                )
        self.GetSubThreads = channel.unary_unary(
                '/ThreadsService/GetSubThreads',
                request_serializer=threads__pb2.GetSubThreadsRequest.SerializeToString,
                response_deserializer=threads__pb2.GetSubThreadsResponse.FromString,
                )
        self.UpdateThreads = channel.unary_unary(
                '/ThreadsService/UpdateThreads',
                request_serializer=threads__pb2.UpdateThreadsRequest.SerializeToString,
                response_deserializer=threads__pb2.UpdateThreadsResponse.FromString,
                )


class ThreadsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProjectThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSubThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateThreads(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ThreadsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProjectThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjectThreads,
                    request_deserializer=threads__pb2.GetProjectThreadsRequest.FromString,
                    response_serializer=threads__pb2.GetProjectThreadsResponse.SerializeToString,
            ),
            'GetSubThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSubThreads,
                    request_deserializer=threads__pb2.GetSubThreadsRequest.FromString,
                    response_serializer=threads__pb2.GetSubThreadsResponse.SerializeToString,
            ),
            'UpdateThreads': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateThreads,
                    request_deserializer=threads__pb2.UpdateThreadsRequest.FromString,
                    response_serializer=threads__pb2.UpdateThreadsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ThreadsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ThreadsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProjectThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ThreadsService/GetProjectThreads',
            threads__pb2.GetProjectThreadsRequest.SerializeToString,
            threads__pb2.GetProjectThreadsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSubThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ThreadsService/GetSubThreads',
            threads__pb2.GetSubThreadsRequest.SerializeToString,
            threads__pb2.GetSubThreadsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateThreads(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ThreadsService/UpdateThreads',
            threads__pb2.UpdateThreadsRequest.SerializeToString,
            threads__pb2.UpdateThreadsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
