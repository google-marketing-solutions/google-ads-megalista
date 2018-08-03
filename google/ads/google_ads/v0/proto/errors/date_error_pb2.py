# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/date_error.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/errors/date_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n5google/ads/googleads_v0/proto/errors/date_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xe0\x02\n\rDateErrorEnum\"\xce\x02\n\tDateError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12 \n\x1cINVALID_FIELD_VALUES_IN_DATE\x10\x02\x12%\n!INVALID_FIELD_VALUES_IN_DATE_TIME\x10\x03\x12\x17\n\x13INVALID_STRING_DATE\x10\x04\x12\x1c\n\x18INVALID_STRING_DATE_TIME\x10\x06\x12\x1d\n\x19\x45\x41RLIER_THAN_MINIMUM_DATE\x10\x07\x12\x1b\n\x17LATER_THAN_MAXIMUM_DATE\x10\x08\x12\x33\n/DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE\x10\t\x12\x32\n.DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL\x10\nB\xc4\x01\n\"com.google.ads.googleads.v0.errorsB\x0e\x44\x61teErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_DATEERRORENUM_DATEERROR = _descriptor.EnumDescriptor(
  name='DateError',
  full_name='google.ads.googleads.v0.errors.DateErrorEnum.DateError',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FIELD_VALUES_IN_DATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FIELD_VALUES_IN_DATE_TIME', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_STRING_DATE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_STRING_DATE_TIME', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EARLIER_THAN_MINIMUM_DATE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATER_THAN_MAXIMUM_DATE', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_RANGE_MINIMUM_DATE_LATER_THAN_MAXIMUM_DATE', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_RANGE_MINIMUM_AND_MAXIMUM_DATES_BOTH_NULL', index=9, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=108,
  serialized_end=442,
)
_sym_db.RegisterEnumDescriptor(_DATEERRORENUM_DATEERROR)


_DATEERRORENUM = _descriptor.Descriptor(
  name='DateErrorEnum',
  full_name='google.ads.googleads.v0.errors.DateErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATEERRORENUM_DATEERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=442,
)

_DATEERRORENUM_DATEERROR.containing_type = _DATEERRORENUM
DESCRIPTOR.message_types_by_name['DateErrorEnum'] = _DATEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DateErrorEnum = _reflection.GeneratedProtocolMessageType('DateErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _DATEERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.date_error_pb2'
  ,
  __doc__ = """Container for enum describing possible date errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.DateErrorEnum)
  ))
_sym_db.RegisterMessage(DateErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\016DateErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
