# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/customer_feed_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/customer_feed_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v0.errorsB\026CustomerFeedErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors\352\002\"Google::Ads::GoogleAds::V0::Errors'),
  serialized_pb=_b('\n>google/ads/googleads_v0/proto/errors/customer_feed_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xf7\x02\n\x15\x43ustomerFeedErrorEnum\"\xdd\x02\n\x11\x43ustomerFeedError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12,\n(FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE\x10\x02\x12\"\n\x1e\x43\x41NNOT_CREATE_FOR_REMOVED_FEED\x10\x03\x12\x30\n,CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED\x10\x04\x12\'\n#CANNOT_MODIFY_REMOVED_CUSTOMER_FEED\x10\x05\x12\x1c\n\x18INVALID_PLACEHOLDER_TYPE\x10\x06\x12,\n(MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE\x10\x07\x12\x31\n-PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED\x10\x08\x42\xf1\x01\n\"com.google.ads.googleads.v0.errorsB\x16\x43ustomerFeedErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errors\xea\x02\"Google::Ads::GoogleAds::V0::Errorsb\x06proto3')
)



_CUSTOMERFEEDERRORENUM_CUSTOMERFEEDERROR = _descriptor.EnumDescriptor(
  name='CustomerFeedError',
  full_name='google.ads.googleads.v0.errors.CustomerFeedErrorEnum.CustomerFeedError',
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
      name='FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_FOR_REMOVED_FEED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_MODIFY_REMOVED_CUSTOMER_FEED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEHOLDER_TYPE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=125,
  serialized_end=474,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMERFEEDERRORENUM_CUSTOMERFEEDERROR)


_CUSTOMERFEEDERRORENUM = _descriptor.Descriptor(
  name='CustomerFeedErrorEnum',
  full_name='google.ads.googleads.v0.errors.CustomerFeedErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMERFEEDERRORENUM_CUSTOMERFEEDERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=474,
)

_CUSTOMERFEEDERRORENUM_CUSTOMERFEEDERROR.containing_type = _CUSTOMERFEEDERRORENUM
DESCRIPTOR.message_types_by_name['CustomerFeedErrorEnum'] = _CUSTOMERFEEDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CustomerFeedErrorEnum = _reflection.GeneratedProtocolMessageType('CustomerFeedErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMERFEEDERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.customer_feed_error_pb2'
  ,
  __doc__ = """Container for enum describing possible customer feed errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.CustomerFeedErrorEnum)
  ))
_sym_db.RegisterMessage(CustomerFeedErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
