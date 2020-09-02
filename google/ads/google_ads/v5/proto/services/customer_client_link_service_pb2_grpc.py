# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v5.proto.resources import customer_client_link_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_customer__client__link__pb2
from google.ads.google_ads.v5.proto.services import customer_client_link_service_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2


class CustomerClientLinkServiceStub(object):
    """Service to manage customer client links.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCustomerClientLink = channel.unary_unary(
                '/google.ads.googleads.v5.services.CustomerClientLinkService/GetCustomerClientLink',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.GetCustomerClientLinkRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_customer__client__link__pb2.CustomerClientLink.FromString,
                )
        self.MutateCustomerClientLink = channel.unary_unary(
                '/google.ads.googleads.v5.services.CustomerClientLinkService/MutateCustomerClientLink',
                request_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.MutateCustomerClientLinkRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.MutateCustomerClientLinkResponse.FromString,
                )


class CustomerClientLinkServiceServicer(object):
    """Service to manage customer client links.
    """

    def GetCustomerClientLink(self, request, context):
        """Returns the requested CustomerClientLink in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateCustomerClientLink(self, request, context):
        """Creates or updates a customer client link. Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CustomerClientLinkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCustomerClientLink': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCustomerClientLink,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.GetCustomerClientLinkRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_customer__client__link__pb2.CustomerClientLink.SerializeToString,
            ),
            'MutateCustomerClientLink': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateCustomerClientLink,
                    request_deserializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.MutateCustomerClientLinkRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.MutateCustomerClientLinkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v5.services.CustomerClientLinkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CustomerClientLinkService(object):
    """Service to manage customer client links.
    """

    @staticmethod
    def GetCustomerClientLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.CustomerClientLinkService/GetCustomerClientLink',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.GetCustomerClientLinkRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_resources_dot_customer__client__link__pb2.CustomerClientLink.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateCustomerClientLink(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v5.services.CustomerClientLinkService/MutateCustomerClientLink',
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.MutateCustomerClientLinkRequest.SerializeToString,
            google_dot_ads_dot_googleads__v5_dot_proto_dot_services_dot_customer__client__link__service__pb2.MutateCustomerClientLinkResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
