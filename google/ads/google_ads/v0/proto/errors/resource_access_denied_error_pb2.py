# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/resource_access_denied_error.proto

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
  name='google/ads/googleads_v0/proto/errors/resource_access_denied_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\nGgoogle/ads/googleads_v0/proto/errors/resource_access_denied_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"s\n\x1dResourceAccessDeniedErrorEnum\"R\n\x19ResourceAccessDeniedError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x17\n\x13WRITE_ACCESS_DENIED\x10\x03\x42\xd4\x01\n\"com.google.ads.googleads.v0.errorsB\x1eResourceAccessDeniedErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_RESOURCEACCESSDENIEDERRORENUM_RESOURCEACCESSDENIEDERROR = _descriptor.EnumDescriptor(
  name='ResourceAccessDeniedError',
  full_name='google.ads.googleads.v0.errors.ResourceAccessDeniedErrorEnum.ResourceAccessDeniedError',
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
      name='WRITE_ACCESS_DENIED', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_RESOURCEACCESSDENIEDERRORENUM_RESOURCEACCESSDENIEDERROR)


_RESOURCEACCESSDENIEDERRORENUM = _descriptor.Descriptor(
  name='ResourceAccessDeniedErrorEnum',
  full_name='google.ads.googleads.v0.errors.ResourceAccessDeniedErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESOURCEACCESSDENIEDERRORENUM_RESOURCEACCESSDENIEDERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=222,
)

_RESOURCEACCESSDENIEDERRORENUM_RESOURCEACCESSDENIEDERROR.containing_type = _RESOURCEACCESSDENIEDERRORENUM
DESCRIPTOR.message_types_by_name['ResourceAccessDeniedErrorEnum'] = _RESOURCEACCESSDENIEDERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceAccessDeniedErrorEnum = _reflection.GeneratedProtocolMessageType('ResourceAccessDeniedErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCEACCESSDENIEDERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.resource_access_denied_error_pb2'
  ,
  __doc__ = """Container for enum describing possible resource access denied errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.ResourceAccessDeniedErrorEnum)
  ))
_sym_db.RegisterMessage(ResourceAccessDeniedErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\036ResourceAccessDeniedErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
