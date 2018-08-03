# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/query_error.proto

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
  name='google/ads/googleads_v0/proto/errors/query_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n6google/ads/googleads_v0/proto/errors/query_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xe4\x0c\n\x0eQueryErrorEnum\"\xd1\x0c\n\nQueryError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0bQUERY_ERROR\x10\x32\x12\x15\n\x11\x42\x41\x44_ENUM_CONSTANT\x10\x12\x12\x17\n\x13\x42\x41\x44_ESCAPE_SEQUENCE\x10\x07\x12\x12\n\x0e\x42\x41\x44_FIELD_NAME\x10\x0c\x12\x13\n\x0f\x42\x41\x44_LIMIT_VALUE\x10\x0f\x12\x0e\n\nBAD_NUMBER\x10\x05\x12\x10\n\x0c\x42\x41\x44_OPERATOR\x10\x03\x12$\n BAD_RESOURCE_TYPE_IN_FROM_CLAUSE\x10-\x12\x0e\n\nBAD_SYMBOL\x10\x02\x12\r\n\tBAD_VALUE\x10\x04\x12\x17\n\x13\x44\x41TE_RANGE_TOO_WIDE\x10$\x12\x10\n\x0c\x45XPECTED_AND\x10\x1e\x12\x0f\n\x0b\x45XPECTED_BY\x10\x0e\x12-\n)EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE\x10%\x12\"\n\x1e\x45XPECTED_FILTERS_ON_DATE_RANGE\x10\x37\x12\x11\n\rEXPECTED_FROM\x10,\x12\x11\n\rEXPECTED_LIST\x10)\x12.\n*EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE\x10\x10\x12\x13\n\x0f\x45XPECTED_SELECT\x10\r\x12\x19\n\x15\x45XPECTED_SINGLE_VALUE\x10*\x12(\n$EXPECTED_VALUE_WITH_BETWEEN_OPERATOR\x10\x1d\x12\x17\n\x13INVALID_DATE_FORMAT\x10&\x12\x18\n\x14INVALID_STRING_VALUE\x10\x39\x12\'\n#INVALID_VALUE_WITH_BETWEEN_OPERATOR\x10\x1a\x12&\n\"INVALID_VALUE_WITH_DURING_OPERATOR\x10\x16\x12$\n INVALID_VALUE_WITH_LIKE_OPERATOR\x10\x38\x12\x1b\n\x17OPERATOR_FIELD_MISMATCH\x10#\x12&\n\"PROHIBITED_EMPTY_LIST_IN_CONDITION\x10\x1c\x12\x1c\n\x18PROHIBITED_ENUM_CONSTANT\x10\x36\x12\x31\n-PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE\x10\x1f\x12\'\n#PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE\x10(\x12%\n!PROHIBITED_FIELD_IN_SELECT_CLAUSE\x10\x17\x12$\n PROHIBITED_FIELD_IN_WHERE_CLAUSE\x10\x18\x12+\n\'PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE\x10+\x12-\n)PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE\x10\x30\x12,\n(PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE\x10:\x12/\n+PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE\x10\x31\x12\x30\n,PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE\x10\x33\x12<\n8PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE\x10\x35\x12\x17\n\x13LIMIT_VALUE_TOO_LOW\x10\x19\x12 \n\x1cPROHIBITED_NEWLINE_IN_STRING\x10\x08\x12(\n$PROHIBITED_VALUE_COMBINATION_IN_LIST\x10\n\x12\x36\n2PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR\x10\x15\x12\x19\n\x15STRING_NOT_TERMINATED\x10\x06\x12\x15\n\x11TOO_MANY_SEGMENTS\x10\"\x12\x1b\n\x17UNEXPECTED_END_OF_QUERY\x10\t\x12\x1a\n\x16UNEXPECTED_FROM_CLAUSE\x10/\x12\x16\n\x12UNRECOGNIZED_FIELD\x10 \x12\x14\n\x10UNEXPECTED_INPUT\x10\x0b\x42\xc5\x01\n\"com.google.ads.googleads.v0.errorsB\x0fQueryErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_QUERYERRORENUM_QUERYERROR = _descriptor.EnumDescriptor(
  name='QueryError',
  full_name='google.ads.googleads.v0.errors.QueryErrorEnum.QueryError',
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
      name='QUERY_ERROR', index=2, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_ENUM_CONSTANT', index=3, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_ESCAPE_SEQUENCE', index=4, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_FIELD_NAME', index=5, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_LIMIT_VALUE', index=6, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_NUMBER', index=7, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_OPERATOR', index=8, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_RESOURCE_TYPE_IN_FROM_CLAUSE', index=9, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_SYMBOL', index=10, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_VALUE', index=11, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_RANGE_TOO_WIDE', index=12, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_AND', index=13, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_BY', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_DIMENSION_FIELD_IN_SELECT_CLAUSE', index=15, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_FILTERS_ON_DATE_RANGE', index=16, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_FROM', index=17, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_LIST', index=18, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_REFERENCED_FIELD_IN_SELECT_CLAUSE', index=19, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_SELECT', index=20, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_SINGLE_VALUE', index=21, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECTED_VALUE_WITH_BETWEEN_OPERATOR', index=22, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DATE_FORMAT', index=23, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_STRING_VALUE', index=24, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_VALUE_WITH_BETWEEN_OPERATOR', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_VALUE_WITH_DURING_OPERATOR', index=26, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_VALUE_WITH_LIKE_OPERATOR', index=27, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPERATOR_FIELD_MISMATCH', index=28, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_EMPTY_LIST_IN_CONDITION', index=29, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_ENUM_CONSTANT', index=30, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_FIELD_COMBINATION_IN_SELECT_CLAUSE', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_FIELD_IN_ORDER_BY_CLAUSE', index=32, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_FIELD_IN_SELECT_CLAUSE', index=33, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_FIELD_IN_WHERE_CLAUSE', index=34, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_RESOURCE_TYPE_IN_FROM_CLAUSE', index=35, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE', index=36, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_RESOURCE_TYPE_IN_WHERE_CLAUSE', index=37, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE', index=38, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_SEGMENT_IN_SELECT_OR_WHERE_CLAUSE', index=39, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_SEGMENT_WITH_METRIC_IN_SELECT_OR_WHERE_CLAUSE', index=40, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIMIT_VALUE_TOO_LOW', index=41, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_NEWLINE_IN_STRING', index=42, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_VALUE_COMBINATION_IN_LIST', index=43, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROHIBITED_VALUE_COMBINATION_WITH_BETWEEN_OPERATOR', index=44, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING_NOT_TERMINATED', index=45, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_SEGMENTS', index=46, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_END_OF_QUERY', index=47, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_FROM_CLAUSE', index=48, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNRECOGNIZED_FIELD', index=49, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNEXPECTED_INPUT', index=50, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=110,
  serialized_end=1727,
)
_sym_db.RegisterEnumDescriptor(_QUERYERRORENUM_QUERYERROR)


_QUERYERRORENUM = _descriptor.Descriptor(
  name='QueryErrorEnum',
  full_name='google.ads.googleads.v0.errors.QueryErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUERYERRORENUM_QUERYERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=1727,
)

_QUERYERRORENUM_QUERYERROR.containing_type = _QUERYERRORENUM
DESCRIPTOR.message_types_by_name['QueryErrorEnum'] = _QUERYERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryErrorEnum = _reflection.GeneratedProtocolMessageType('QueryErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _QUERYERRORENUM,
  __module__ = 'google.ads.googleads_v0.proto.errors.query_error_pb2'
  ,
  __doc__ = """Container for enum describing possible query errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.QueryErrorEnum)
  ))
_sym_db.RegisterMessage(QueryErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\017QueryErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
