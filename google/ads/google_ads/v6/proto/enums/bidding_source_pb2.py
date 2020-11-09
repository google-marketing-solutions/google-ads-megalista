# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/bidding_source.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/bidding_source.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\022BiddingSourceProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/ads/googleads_v6/proto/enums/bidding_source.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\x87\x01\n\x11\x42iddingSourceEnum\"r\n\rBiddingSource\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1d\n\x19\x43\x41MPAIGN_BIDDING_STRATEGY\x10\x05\x12\x0c\n\x08\x41\x44_GROUP\x10\x06\x12\x16\n\x12\x41\x44_GROUP_CRITERION\x10\x07\x42\xe7\x01\n!com.google.ads.googleads.v6.enumsB\x12\x42iddingSourceProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_BIDDINGSOURCEENUM_BIDDINGSOURCE = _descriptor.EnumDescriptor(
  name='BiddingSource',
  full_name='google.ads.googleads.v6.enums.BiddingSourceEnum.BiddingSource',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_BIDDING_STRATEGY', index=2, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP', index=3, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_CRITERION', index=4, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=143,
  serialized_end=257,
)
_sym_db.RegisterEnumDescriptor(_BIDDINGSOURCEENUM_BIDDINGSOURCE)


_BIDDINGSOURCEENUM = _descriptor.Descriptor(
  name='BiddingSourceEnum',
  full_name='google.ads.googleads.v6.enums.BiddingSourceEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BIDDINGSOURCEENUM_BIDDINGSOURCE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=257,
)

_BIDDINGSOURCEENUM_BIDDINGSOURCE.containing_type = _BIDDINGSOURCEENUM
DESCRIPTOR.message_types_by_name['BiddingSourceEnum'] = _BIDDINGSOURCEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BiddingSourceEnum = _reflection.GeneratedProtocolMessageType('BiddingSourceEnum', (_message.Message,), {
  'DESCRIPTOR' : _BIDDINGSOURCEENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.bidding_source_pb2'
  ,
  '__doc__': """Container for enum describing possible bidding sources.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.BiddingSourceEnum)
  })
_sym_db.RegisterMessage(BiddingSourceEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
