# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v0.proto.services import google_ads_service_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_google__ads__service__pb2


class GoogleAdsServiceStub(object):
  """Service to fetch data and metrics across resources.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Search = channel.unary_unary(
        '/google.ads.googleads.v0.services.GoogleAdsService/Search',
        request_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsResponse.FromString,
        )


class GoogleAdsServiceServicer(object):
  """Service to fetch data and metrics across resources.
  """

  def Search(self, request, context):
    """Returns all rows that match the search query.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GoogleAdsServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Search': grpc.unary_unary_rpc_method_handler(
          servicer.Search,
          request_deserializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v0_dot_proto_dot_services_dot_google__ads__service__pb2.SearchGoogleAdsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v0.services.GoogleAdsService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
