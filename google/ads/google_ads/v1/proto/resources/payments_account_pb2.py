# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/resources/payments_account.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/resources/payments_account.proto',
  package='google.ads.googleads.v1.resources',
  syntax='proto3',
  serialized_options=_b('\n%com.google.ads.googleads.v1.resourcesB\024PaymentsAccountProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V1.Resources\312\002!Google\\Ads\\GoogleAds\\V1\\Resources\352\002%Google::Ads::GoogleAds::V1::Resources'),
  serialized_pb=_b('\n>google/ads/googleads_v1/proto/resources/payments_account.proto\x12!google.ads.googleads.v1.resources\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\"\xc4\x02\n\x0fPaymentsAccount\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x39\n\x13payments_account_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rcurrency_code\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x13payments_profile_id\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x43\n\x1dsecondary_payments_profile_id\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x81\x02\n%com.google.ads.googleads.v1.resourcesB\x14PaymentsAccountProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v1/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V1.Resources\xca\x02!Google\\Ads\\GoogleAds\\V1\\Resources\xea\x02%Google::Ads::GoogleAds::V1::Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_PAYMENTSACCOUNT = _descriptor.Descriptor(
  name='PaymentsAccount',
  full_name='google.ads.googleads.v1.resources.PaymentsAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.resources.PaymentsAccount.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_account_id', full_name='google.ads.googleads.v1.resources.PaymentsAccount.payments_account_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v1.resources.PaymentsAccount.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v1.resources.PaymentsAccount.currency_code', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payments_profile_id', full_name='google.ads.googleads.v1.resources.PaymentsAccount.payments_profile_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secondary_payments_profile_id', full_name='google.ads.googleads.v1.resources.PaymentsAccount.secondary_payments_profile_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=488,
)

_PAYMENTSACCOUNT.fields_by_name['payments_account_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PAYMENTSACCOUNT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PAYMENTSACCOUNT.fields_by_name['currency_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PAYMENTSACCOUNT.fields_by_name['payments_profile_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PAYMENTSACCOUNT.fields_by_name['secondary_payments_profile_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['PaymentsAccount'] = _PAYMENTSACCOUNT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaymentsAccount = _reflection.GeneratedProtocolMessageType('PaymentsAccount', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTSACCOUNT,
  __module__ = 'google.ads.googleads_v1.proto.resources.payments_account_pb2'
  ,
  __doc__ = """A Payments account, which can be used to set up billing for an Ads
  customer.
  
  
  Attributes:
      resource_name:
          The resource name of the Payments account. PaymentsAccount
          resource names have the form:  ``customers/{customer_id}/payme
          ntsAccounts/{payments_account_id}``
      payments_account_id:
          A 16 digit ID used to identify a Payments account.
      name:
          The name of the Payments account.
      currency_code:
          The currency code of the Payments account. A subset of the
          currency codes derived from the ISO 4217 standard is
          supported.
      payments_profile_id:
          A 12 digit ID used to identify the Payments profile associated
          with the Payments account.
      secondary_payments_profile_id:
          A secondary Payments profile ID present in uncommon
          situations, e.g. when a sequential liability agreement has
          been arranged.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.resources.PaymentsAccount)
  ))
_sym_db.RegisterMessage(PaymentsAccount)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
