# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v6/proto/errors/feed_item_set_error.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v6/proto/errors/feed_item_set_error.proto',
  package='google.ads.googleads.v6.errors',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v6.errorsB\025FeedItemSetErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V6.Errors\312\002\036Google\\Ads\\GoogleAds\\V6\\Errors\352\002\"Google::Ads::GoogleAds::V6::Errors',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n>google/ads/googleads_v6/proto/errors/feed_item_set_error.proto\x12\x1egoogle.ads.googleads.v6.errors\x1a\x1cgoogle/api/annotations.proto\"\xfa\x01\n\x14\x46\x65\x65\x64ItemSetErrorEnum\"\xe1\x01\n\x10\x46\x65\x65\x64ItemSetError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x19\n\x15\x46\x45\x45\x44_ITEM_SET_REMOVED\x10\x02\x12\x1f\n\x1b\x43\x41NNOT_CLEAR_DYNAMIC_FILTER\x10\x03\x12 \n\x1c\x43\x41NNOT_CREATE_DYNAMIC_FILTER\x10\x04\x12\x15\n\x11INVALID_FEED_TYPE\x10\x05\x12\x12\n\x0e\x44UPLICATE_NAME\x10\x06\x12&\n\"WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE\x10\x07\x42\xf0\x01\n\"com.google.ads.googleads.v6.errorsB\x15\x46\x65\x65\x64ItemSetErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v6/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V6.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V6\\Errors\xea\x02\"Google::Ads::GoogleAds::V6::Errorsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FEEDITEMSETERRORENUM_FEEDITEMSETERROR = _descriptor.EnumDescriptor(
  name='FeedItemSetError',
  full_name='google.ads.googleads.v6.errors.FeedItemSetErrorEnum.FeedItemSetError',
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
      name='FEED_ITEM_SET_REMOVED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CLEAR_DYNAMIC_FILTER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_DYNAMIC_FILTER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FEED_TYPE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DUPLICATE_NAME', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=379,
)
_sym_db.RegisterEnumDescriptor(_FEEDITEMSETERRORENUM_FEEDITEMSETERROR)


_FEEDITEMSETERRORENUM = _descriptor.Descriptor(
  name='FeedItemSetErrorEnum',
  full_name='google.ads.googleads.v6.errors.FeedItemSetErrorEnum',
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
    _FEEDITEMSETERRORENUM_FEEDITEMSETERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=379,
)

_FEEDITEMSETERRORENUM_FEEDITEMSETERROR.containing_type = _FEEDITEMSETERRORENUM
DESCRIPTOR.message_types_by_name['FeedItemSetErrorEnum'] = _FEEDITEMSETERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedItemSetErrorEnum = _reflection.GeneratedProtocolMessageType('FeedItemSetErrorEnum', (_message.Message,), {
  'DESCRIPTOR' : _FEEDITEMSETERRORENUM,
  '__module__' : 'google.ads.googleads_v6.proto.errors.feed_item_set_error_pb2'
  ,
  '__doc__': """Container for enum describing possible feed item set errors.""",
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v6.errors.FeedItemSetErrorEnum)
  })
_sym_db.RegisterMessage(FeedItemSetErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
