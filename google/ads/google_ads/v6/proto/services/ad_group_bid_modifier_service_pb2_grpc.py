# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import ad_group_bid_modifier_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2
from google.ads.google_ads.v6.proto.services import ad_group_bid_modifier_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2


class AdGroupBidModifierServiceStub(object):
    """Proto file describing the Ad Group Bid Modifier service.

    Service to manage ad group bid modifiers.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAdGroupBidModifier = channel.unary_unary(
                '/google.ads.googleads.v6.services.AdGroupBidModifierService/GetAdGroupBidModifier',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.GetAdGroupBidModifierRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2.AdGroupBidModifier.FromString,
                )
        self.MutateAdGroupBidModifiers = channel.unary_unary(
                '/google.ads.googleads.v6.services.AdGroupBidModifierService/MutateAdGroupBidModifiers',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.MutateAdGroupBidModifiersRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.MutateAdGroupBidModifiersResponse.FromString,
                )


class AdGroupBidModifierServiceServicer(object):
    """Proto file describing the Ad Group Bid Modifier service.

    Service to manage ad group bid modifiers.
    """

    def GetAdGroupBidModifier(self, request, context):
        """Returns the requested ad group bid modifier in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateAdGroupBidModifiers(self, request, context):
        """Creates, updates, or removes ad group bid modifiers.
        Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdGroupBidModifierServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAdGroupBidModifier': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAdGroupBidModifier,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.GetAdGroupBidModifierRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2.AdGroupBidModifier.SerializeToString,
            ),
            'MutateAdGroupBidModifiers': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateAdGroupBidModifiers,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.MutateAdGroupBidModifiersRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.MutateAdGroupBidModifiersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.AdGroupBidModifierService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdGroupBidModifierService(object):
    """Proto file describing the Ad Group Bid Modifier service.

    Service to manage ad group bid modifiers.
    """

    @staticmethod
    def GetAdGroupBidModifier(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AdGroupBidModifierService/GetAdGroupBidModifier',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.GetAdGroupBidModifierRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__bid__modifier__pb2.AdGroupBidModifier.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateAdGroupBidModifiers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AdGroupBidModifierService/MutateAdGroupBidModifiers',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.MutateAdGroupBidModifiersRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__bid__modifier__service__pb2.MutateAdGroupBidModifiersResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
