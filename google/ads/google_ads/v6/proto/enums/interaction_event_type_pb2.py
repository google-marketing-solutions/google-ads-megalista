# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/interaction_event_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/interaction_event_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\031InteractionEventTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@google/ads/googleads_v6/proto/enums/interaction_event_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\x85\x01\n\x18InteractionEventTypeEnum\"i\n\x14InteractionEventType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\t\n\x05\x43LICK\x10\x02\x12\x0e\n\nENGAGEMENT\x10\x03\x12\x0e\n\nVIDEO_VIEW\x10\x04\x12\x08\n\x04NONE\x10\x05\x42\xee\x01\n!com.google.ads.googleads.v6.enumsB\x19InteractionEventTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_INTERACTIONEVENTTYPEENUM_INTERACTIONEVENTTYPE = _descriptor.EnumDescriptor(
  name='InteractionEventType',
  full_name='google.ads.googleads.v6.enums.InteractionEventTypeEnum.InteractionEventType',
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
      name='CLICK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENGAGEMENT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIDEO_VIEW', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=158,
  serialized_end=263,
)
_sym_db.RegisterEnumDescriptor(_INTERACTIONEVENTTYPEENUM_INTERACTIONEVENTTYPE)


_INTERACTIONEVENTTYPEENUM = _descriptor.Descriptor(
  name='InteractionEventTypeEnum',
  full_name='google.ads.googleads.v6.enums.InteractionEventTypeEnum',
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
    _INTERACTIONEVENTTYPEENUM_INTERACTIONEVENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=263,
)

_INTERACTIONEVENTTYPEENUM_INTERACTIONEVENTTYPE.containing_type = _INTERACTIONEVENTTYPEENUM
DESCRIPTOR.message_types_by_name['InteractionEventTypeEnum'] = _INTERACTIONEVENTTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InteractionEventTypeEnum = _reflection.GeneratedProtocolMessageType('InteractionEventTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _INTERACTIONEVENTTYPEENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.interaction_event_type_pb2'
  ,
  '__doc__': """Container for enum describing types of payable and free interactions.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.InteractionEventTypeEnum)
  })
_sym_db.RegisterMessage(InteractionEventTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
