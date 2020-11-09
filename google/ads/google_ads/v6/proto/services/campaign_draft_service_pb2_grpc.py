# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import campaign_draft_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__draft__pb2
from google.ads.google_ads.v6.proto.services import campaign_draft_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


class CampaignDraftServiceStub(object):
    """Proto file describing the Campaign Draft service.

    Service to manage campaign drafts.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetCampaignDraft = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignDraftService/GetCampaignDraft',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.GetCampaignDraftRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__draft__pb2.CampaignDraft.FromString,
                )
        self.MutateCampaignDrafts = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignDraftService/MutateCampaignDrafts',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.MutateCampaignDraftsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.MutateCampaignDraftsResponse.FromString,
                )
        self.PromoteCampaignDraft = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignDraftService/PromoteCampaignDraft',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.PromoteCampaignDraftRequest.SerializeToString,
                response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString,
                )
        self.ListCampaignDraftAsyncErrors = channel.unary_unary(
                '/google.ads.googleads.v6.services.CampaignDraftService/ListCampaignDraftAsyncErrors',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.ListCampaignDraftAsyncErrorsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.ListCampaignDraftAsyncErrorsResponse.FromString,
                )


class CampaignDraftServiceServicer(object):
    """Proto file describing the Campaign Draft service.

    Service to manage campaign drafts.
    """

    def GetCampaignDraft(self, request, context):
        """Returns the requested campaign draft in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateCampaignDrafts(self, request, context):
        """Creates, updates, or removes campaign drafts. Operation statuses are
        returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PromoteCampaignDraft(self, request, context):
        """Promotes the changes in a draft back to the base campaign.

        This method returns a Long Running Operation (LRO) indicating if the
        Promote is done. Use [Operations.GetOperation] to poll the LRO until it
        is done. Only a done status is returned in the response. See the status
        in the Campaign Draft resource to determine if the promotion was
        successful. If the LRO failed, use
        [CampaignDraftService.ListCampaignDraftAsyncErrors][google.ads.googleads.v6.services.CampaignDraftService.ListCampaignDraftAsyncErrors] to view the list of
        error reasons.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListCampaignDraftAsyncErrors(self, request, context):
        """Returns all errors that occurred during CampaignDraft promote. Throws an
        error if called before campaign draft is promoted.
        Supports standard list paging.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CampaignDraftServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetCampaignDraft': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCampaignDraft,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.GetCampaignDraftRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__draft__pb2.CampaignDraft.SerializeToString,
            ),
            'MutateCampaignDrafts': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateCampaignDrafts,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.MutateCampaignDraftsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.MutateCampaignDraftsResponse.SerializeToString,
            ),
            'PromoteCampaignDraft': grpc.unary_unary_rpc_method_handler(
                    servicer.PromoteCampaignDraft,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.PromoteCampaignDraftRequest.FromString,
                    response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString,
            ),
            'ListCampaignDraftAsyncErrors': grpc.unary_unary_rpc_method_handler(
                    servicer.ListCampaignDraftAsyncErrors,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.ListCampaignDraftAsyncErrorsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.ListCampaignDraftAsyncErrorsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.CampaignDraftService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CampaignDraftService(object):
    """Proto file describing the Campaign Draft service.

    Service to manage campaign drafts.
    """

    @staticmethod
    def GetCampaignDraft(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignDraftService/GetCampaignDraft',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.GetCampaignDraftRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_campaign__draft__pb2.CampaignDraft.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateCampaignDrafts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignDraftService/MutateCampaignDrafts',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.MutateCampaignDraftsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.MutateCampaignDraftsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PromoteCampaignDraft(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignDraftService/PromoteCampaignDraft',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.PromoteCampaignDraftRequest.SerializeToString,
            google_dot_longrunning_dot_operations__pb2.Operation.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListCampaignDraftAsyncErrors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.CampaignDraftService/ListCampaignDraftAsyncErrors',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.ListCampaignDraftAsyncErrorsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_campaign__draft__service__pb2.ListCampaignDraftAsyncErrorsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
