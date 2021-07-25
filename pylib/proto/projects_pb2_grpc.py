# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import projects_pb2 as projects__pb2


class ProjectsServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetProjects = channel.unary_unary(
                '/ProjectsService/GetProjects',
                request_serializer=projects__pb2.GetProjectsRequest.SerializeToString,
                response_deserializer=projects__pb2.GetProjectsResponse.FromString,
                )
        self.GetProjectDetails = channel.unary_unary(
                '/ProjectsService/GetProjectDetails',
                request_serializer=projects__pb2.GetProjectDetailsRequest.SerializeToString,
                response_deserializer=projects__pb2.GetProjectDetailsResponse.FromString,
                )
        self.UpdateProjectDetails = channel.unary_unary(
                '/ProjectsService/UpdateProjectDetails',
                request_serializer=projects__pb2.UpdateProjectDetailsRequest.SerializeToString,
                response_deserializer=projects__pb2.UpdateProjectDetailsResponse.FromString,
                )


class ProjectsServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetProjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjectDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectDetails(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjects,
                    request_deserializer=projects__pb2.GetProjectsRequest.FromString,
                    response_serializer=projects__pb2.GetProjectsResponse.SerializeToString,
            ),
            'GetProjectDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProjectDetails,
                    request_deserializer=projects__pb2.GetProjectDetailsRequest.FromString,
                    response_serializer=projects__pb2.GetProjectDetailsResponse.SerializeToString,
            ),
            'UpdateProjectDetails': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProjectDetails,
                    request_deserializer=projects__pb2.UpdateProjectDetailsRequest.FromString,
                    response_serializer=projects__pb2.UpdateProjectDetailsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ProjectsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectsService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProjectsService/GetProjects',
            projects__pb2.GetProjectsRequest.SerializeToString,
            projects__pb2.GetProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProjectDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProjectsService/GetProjectDetails',
            projects__pb2.GetProjectDetailsRequest.SerializeToString,
            projects__pb2.GetProjectDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProjectDetails(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ProjectsService/UpdateProjectDetails',
            projects__pb2.UpdateProjectDetailsRequest.SerializeToString,
            projects__pb2.UpdateProjectDetailsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)