# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/enums/campaign_draft_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/enums/campaign_draft_status.proto',
  package='google.ads.googleads.v1.enums',
  syntax='proto3',
  serialized_options=_b('\n!com.google.ads.googleads.v1.enumsB\030CampaignDraftStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V1.Enums\312\002\035Google\\Ads\\GoogleAds\\V1\\Enums\352\002!Google::Ads::GoogleAds::V1::Enums'),
  serialized_pb=_b('\n?google/ads/googleads_v1/proto/enums/campaign_draft_status.proto\x12\x1dgoogle.ads.googleads.v1.enums\x1a\x1cgoogle/api/annotations.proto\"\x9a\x01\n\x17\x43\x61mpaignDraftStatusEnum\"\x7f\n\x13\x43\x61mpaignDraftStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08PROPOSED\x10\x02\x12\x0b\n\x07REMOVED\x10\x03\x12\r\n\tPROMOTING\x10\x05\x12\x0c\n\x08PROMOTED\x10\x04\x12\x12\n\x0ePROMOTE_FAILED\x10\x06\x42\xed\x01\n!com.google.ads.googleads.v1.enumsB\x18\x43\x61mpaignDraftStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v1/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V1.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V1\\Enums\xea\x02!Google::Ads::GoogleAds::V1::Enumsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CAMPAIGNDRAFTSTATUSENUM_CAMPAIGNDRAFTSTATUS = _descriptor.EnumDescriptor(
  name='CampaignDraftStatus',
  full_name='google.ads.googleads.v1.enums.CampaignDraftStatusEnum.CampaignDraftStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROPOSED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTING', index=4, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTED', index=5, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTE_FAILED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=156,
  serialized_end=283,
)
_sym_db.RegisterEnumDescriptor(_CAMPAIGNDRAFTSTATUSENUM_CAMPAIGNDRAFTSTATUS)


_CAMPAIGNDRAFTSTATUSENUM = _descriptor.Descriptor(
  name='CampaignDraftStatusEnum',
  full_name='google.ads.googleads.v1.enums.CampaignDraftStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMPAIGNDRAFTSTATUSENUM_CAMPAIGNDRAFTSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=283,
)

_CAMPAIGNDRAFTSTATUSENUM_CAMPAIGNDRAFTSTATUS.containing_type = _CAMPAIGNDRAFTSTATUSENUM
DESCRIPTOR.message_types_by_name['CampaignDraftStatusEnum'] = _CAMPAIGNDRAFTSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CampaignDraftStatusEnum = _reflection.GeneratedProtocolMessageType('CampaignDraftStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _CAMPAIGNDRAFTSTATUSENUM,
  __module__ = 'google.ads.googleads_v1.proto.enums.campaign_draft_status_pb2'
  ,
  __doc__ = """Container for enum describing possible statuses of a campaign draft.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.enums.CampaignDraftStatusEnum)
  ))
_sym_db.RegisterMessage(CampaignDraftStatusEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
