# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/errors/extension_feed_item_error.proto

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
  name='google/ads/googleads_v1/proto/errors/extension_feed_item_error.proto',
  package='google.ads.googleads.v1.errors',
  syntax='proto3',
  serialized_options=_b('\n\"com.google.ads.googleads.v1.errorsB\033ExtensionFeedItemErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V1.Errors\312\002\036Google\\Ads\\GoogleAds\\V1\\Errors\352\002\"Google::Ads::GoogleAds::V1::Errors'),
  serialized_pb=_b('\nDgoogle/ads/googleads_v1/proto/errors/extension_feed_item_error.proto\x12\x1egoogle.ads.googleads.v1.errors\x1a\x1cgoogle/api/annotations.proto\"\xad\r\n\x1a\x45xtensionFeedItemErrorEnum\"\x8e\r\n\x16\x45xtensionFeedItemError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12VALUE_OUT_OF_RANGE\x10\x02\x12\x15\n\x11URL_LIST_TOO_LONG\x10\x03\x12\x32\n.CANNOT_HAVE_RESTRICTION_ON_EMPTY_GEO_TARGETING\x10\x04\x12\x1e\n\x1a\x43\x41NNOT_SET_WITH_FINAL_URLS\x10\x05\x12!\n\x1d\x43\x41NNOT_SET_WITHOUT_FINAL_URLS\x10\x06\x12\x18\n\x14INVALID_PHONE_NUMBER\x10\x07\x12*\n&PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY\x10\x08\x12-\n)CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED\x10\t\x12#\n\x1fPREMIUM_RATE_NUMBER_NOT_ALLOWED\x10\n\x12\x1a\n\x16\x44ISALLOWED_NUMBER_TYPE\x10\x0b\x12(\n$INVALID_DOMESTIC_PHONE_NUMBER_FORMAT\x10\x0c\x12#\n\x1fVANITY_PHONE_NUMBER_NOT_ALLOWED\x10\r\x12\"\n\x1eINVALID_CALL_CONVERSION_ACTION\x10\x0e\x12-\n)CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING\x10\x0f\x12*\n&CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY\x10\x10\x12\x30\n,CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED\x10\x11\x12\x12\n\x0eINVALID_APP_ID\x10\x12\x12&\n\"QUOTES_IN_REVIEW_EXTENSION_SNIPPET\x10\x13\x12\'\n#HYPHENS_IN_REVIEW_EXTENSION_SNIPPET\x10\x14\x12&\n\"REVIEW_EXTENSION_SOURCE_INELIGIBLE\x10\x15\x12(\n$SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT\x10\x16\x12\x1f\n\x1bINCONSISTENT_CURRENCY_CODES\x10\x17\x12*\n&PRICE_EXTENSION_HAS_DUPLICATED_HEADERS\x10\x18\x12\x34\n0PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION\x10\x19\x12%\n!PRICE_EXTENSION_HAS_TOO_FEW_ITEMS\x10\x1a\x12&\n\"PRICE_EXTENSION_HAS_TOO_MANY_ITEMS\x10\x1b\x12\x15\n\x11UNSUPPORTED_VALUE\x10\x1c\x12*\n&UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE\x10\x1d\x12\x1d\n\x19INVALID_DEVICE_PREFERENCE\x10\x1e\x12\x18\n\x14INVALID_SCHEDULE_END\x10\x1f\x12*\n&DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE\x10 \x12\x1b\n\x17INVALID_SNIPPETS_HEADER\x10!\x12\'\n#CANNOT_OPERATE_ON_REMOVED_FEED_ITEM\x10\"\x12<\n8PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY\x10#\x12(\n$CONFLICTING_CALL_CONVERSION_SETTINGS\x10$\x12\x1b\n\x17\x45XTENSION_TYPE_MISMATCH\x10%\x12\x1e\n\x1a\x45XTENSION_SUBTYPE_REQUIRED\x10&\x12\x1e\n\x1a\x45XTENSION_TYPE_UNSUPPORTED\x10\'\x12\x31\n-CANNOT_OPERATE_ON_FEED_WITH_MULTIPLE_MAPPINGS\x10(\x12.\n*CANNOT_OPERATE_ON_FEED_WITH_KEY_ATTRIBUTES\x10)\x12\x18\n\x14INVALID_PRICE_FORMAT\x10*\x12\x1a\n\x16PROMOTION_INVALID_TIME\x10+\x12%\n!TOO_MANY_DECIMAL_PLACES_SPECIFIED\x10,B\xf6\x01\n\"com.google.ads.googleads.v1.errorsB\x1b\x45xtensionFeedItemErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v1/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V1.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V1\\Errors\xea\x02\"Google::Ads::GoogleAds::V1::Errorsb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_EXTENSIONFEEDITEMERRORENUM_EXTENSIONFEEDITEMERROR = _descriptor.EnumDescriptor(
  name='ExtensionFeedItemError',
  full_name='google.ads.googleads.v1.errors.ExtensionFeedItemErrorEnum.ExtensionFeedItemError',
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
      name='VALUE_OUT_OF_RANGE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='URL_LIST_TOO_LONG', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_HAVE_RESTRICTION_ON_EMPTY_GEO_TARGETING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_WITH_FINAL_URLS', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_WITHOUT_FINAL_URLS', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PHONE_NUMBER', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_FOR_COUNTRY', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CARRIER_SPECIFIC_SHORT_NUMBER_NOT_ALLOWED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREMIUM_RATE_NUMBER_NOT_ALLOWED', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISALLOWED_NUMBER_TYPE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DOMESTIC_PHONE_NUMBER_FORMAT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VANITY_PHONE_NUMBER_NOT_ALLOWED', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CALL_CONVERSION_ACTION', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_NOT_WHITELISTED_FOR_CALLTRACKING', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALLTRACKING_NOT_SUPPORTED_FOR_COUNTRY', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOMER_CONSENT_FOR_CALL_RECORDING_REQUIRED', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_APP_ID', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUOTES_IN_REVIEW_EXTENSION_SNIPPET', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HYPHENS_IN_REVIEW_EXTENSION_SNIPPET', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVIEW_EXTENSION_SOURCE_INELIGIBLE', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOURCE_NAME_IN_REVIEW_EXTENSION_TEXT', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INCONSISTENT_CURRENCY_CODES', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_DUPLICATED_HEADERS', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_ITEM_HAS_DUPLICATED_HEADER_AND_DESCRIPTION', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_TOO_FEW_ITEMS', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRICE_EXTENSION_HAS_TOO_MANY_ITEMS', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_VALUE', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSUPPORTED_VALUE_IN_SELECTED_LANGUAGE', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_DEVICE_PREFERENCE', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SCHEDULE_END', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_TIME_MUST_BE_IN_ACCOUNT_TIME_ZONE', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SNIPPETS_HEADER', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_REMOVED_FEED_ITEM', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER_NOT_SUPPORTED_WITH_CALLTRACKING_FOR_COUNTRY', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFLICTING_CALL_CONVERSION_SETTINGS', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSION_TYPE_MISMATCH', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSION_SUBTYPE_REQUIRED', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXTENSION_TYPE_UNSUPPORTED', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_FEED_WITH_MULTIPLE_MAPPINGS', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_OPERATE_ON_FEED_WITH_KEY_ATTRIBUTES', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRICE_FORMAT', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROMOTION_INVALID_TIME', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOO_MANY_DECIMAL_PLACES_SPECIFIED', index=44, number=44,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=166,
  serialized_end=1844,
)
_sym_db.RegisterEnumDescriptor(_EXTENSIONFEEDITEMERRORENUM_EXTENSIONFEEDITEMERROR)


_EXTENSIONFEEDITEMERRORENUM = _descriptor.Descriptor(
  name='ExtensionFeedItemErrorEnum',
  full_name='google.ads.googleads.v1.errors.ExtensionFeedItemErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EXTENSIONFEEDITEMERRORENUM_EXTENSIONFEEDITEMERROR,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=1844,
)

_EXTENSIONFEEDITEMERRORENUM_EXTENSIONFEEDITEMERROR.containing_type = _EXTENSIONFEEDITEMERRORENUM
DESCRIPTOR.message_types_by_name['ExtensionFeedItemErrorEnum'] = _EXTENSIONFEEDITEMERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtensionFeedItemErrorEnum = _reflection.GeneratedProtocolMessageType('ExtensionFeedItemErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _EXTENSIONFEEDITEMERRORENUM,
  __module__ = 'google.ads.googleads_v1.proto.errors.extension_feed_item_error_pb2'
  ,
  __doc__ = """Container for enum describing possible extension feed item error.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.errors.ExtensionFeedItemErrorEnum)
  ))
_sym_db.RegisterMessage(ExtensionFeedItemErrorEnum)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
