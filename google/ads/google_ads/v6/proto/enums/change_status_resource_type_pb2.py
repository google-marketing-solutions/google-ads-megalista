# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/enums/change_status_resource_type.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/enums/change_status_resource_type.proto',
  package='google.ads.googleads.v6.enums',
  syntax='proto3',
  serialized_options=b'\n!com.google.ads.googleads.v6.enumsB\035ChangeStatusResourceTypeProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V6.Enums\312\002\035Google\\Ads\\GoogleAds\\V6\\Enums\352\002!Google::Ads::GoogleAds::V6::Enums',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nEgoogle/ads/googleads_v6/proto/enums/change_status_resource_type.proto\x12\x1dgoogle.ads.googleads.v6.enums\x1a\x1cgoogle/api/annotations.proto\"\x90\x02\n\x1c\x43hangeStatusResourceTypeEnum\"\xef\x01\n\x18\x43hangeStatusResourceType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08\x41\x44_GROUP\x10\x03\x12\x0f\n\x0b\x41\x44_GROUP_AD\x10\x04\x12\x16\n\x12\x41\x44_GROUP_CRITERION\x10\x05\x12\x0c\n\x08\x43\x41MPAIGN\x10\x06\x12\x16\n\x12\x43\x41MPAIGN_CRITERION\x10\x07\x12\x08\n\x04\x46\x45\x45\x44\x10\t\x12\r\n\tFEED_ITEM\x10\n\x12\x11\n\rAD_GROUP_FEED\x10\x0b\x12\x11\n\rCAMPAIGN_FEED\x10\x0c\x12\x19\n\x15\x41\x44_GROUP_BID_MODIFIER\x10\rB\xf2\x01\n!com.google.ads.googleads.v6.enumsB\x1d\x43hangeStatusResourceTypeProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v6/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V6.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V6\\Enums\xea\x02!Google::Ads::GoogleAds::V6::Enumsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_CHANGESTATUSRESOURCETYPEENUM_CHANGESTATUSRESOURCETYPE = _descriptor.EnumDescriptor(
  name='ChangeStatusResourceType',
  full_name='google.ads.googleads.v6.enums.ChangeStatusResourceTypeEnum.ChangeStatusResourceType',
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
      name='AD_GROUP', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_AD', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_CRITERION', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_CRITERION', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEED', index=7, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEED_ITEM', index=8, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_FEED', index=9, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CAMPAIGN_FEED', index=10, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AD_GROUP_BID_MODIFIER', index=11, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=168,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_CHANGESTATUSRESOURCETYPEENUM_CHANGESTATUSRESOURCETYPE)


_CHANGESTATUSRESOURCETYPEENUM = _descriptor.Descriptor(
  name='ChangeStatusResourceTypeEnum',
  full_name='google.ads.googleads.v6.enums.ChangeStatusResourceTypeEnum',
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
    _CHANGESTATUSRESOURCETYPEENUM_CHANGESTATUSRESOURCETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=407,
)

_CHANGESTATUSRESOURCETYPEENUM_CHANGESTATUSRESOURCETYPE.containing_type = _CHANGESTATUSRESOURCETYPEENUM
DESCRIPTOR.message_types_by_name['ChangeStatusResourceTypeEnum'] = _CHANGESTATUSRESOURCETYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChangeStatusResourceTypeEnum = _reflection.GeneratedProtocolMessageType('ChangeStatusResourceTypeEnum', (_message.Message,), {
  'DESCRIPTOR' : _CHANGESTATUSRESOURCETYPEENUM,
  '__module__' : 'google.ads.googleads_v6.proto.enums.change_status_resource_type_pb2'
  ,
  '__doc__': """Container for enum describing supported resource types for the
  ChangeStatus resource.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.enums.ChangeStatusResourceTypeEnum)
  })
_sym_db.RegisterMessage(ChangeStatusResourceTypeEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
