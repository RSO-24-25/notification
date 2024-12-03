# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import email_pb2 as email__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in email_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EmailServiceStub(object):
    """The email service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendEmail = channel.unary_unary(
                '/emailservice.EmailService/SendEmail',
                request_serializer=email__pb2.EmailRequest.SerializeToString,
                response_deserializer=email__pb2.EmailResponse.FromString,
                _registered_method=True)


class EmailServiceServicer(object):
    """The email service definition.
    """

    def SendEmail(self, request, context):
        """Sends an email notification
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EmailServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendEmail': grpc.unary_unary_rpc_method_handler(
                    servicer.SendEmail,
                    request_deserializer=email__pb2.EmailRequest.FromString,
                    response_serializer=email__pb2.EmailResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'emailservice.EmailService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('emailservice.EmailService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EmailService(object):
    """The email service definition.
    """

    @staticmethod
    def SendEmail(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/emailservice.EmailService/SendEmail',
            email__pb2.EmailRequest.SerializeToString,
            email__pb2.EmailResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
