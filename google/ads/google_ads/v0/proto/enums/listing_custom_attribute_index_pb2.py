# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/listing_custom_attribute_index.proto

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
  name='google/ads/googleads_v0/proto/enums/listing_custom_attribute_index.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\nHgoogle/ads/googleads_v0/proto/enums/listing_custom_attribute_index.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xd7\x01\n\x1fListingCustomAttributeIndexEnum\"\xb3\x01\n\x1bListingCustomAttributeIndex\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x16\n\x12\x43USTOM_ATTRIBUTE_0\x10\x02\x12\x16\n\x12\x43USTOM_ATTRIBUTE_1\x10\x03\x12\x16\n\x12\x43USTOM_ATTRIBUTE_2\x10\x04\x12\x16\n\x12\x43USTOM_ATTRIBUTE_3\x10\x05\x12\x16\n\x12\x43USTOM_ATTRIBUTE_4\x10\x06\x42\xd1\x01\n!com.google.ads.googleads.v0.enumsB ListingCustomAttributeIndexProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX = _descriptor.EnumDescriptor(
  name='ListingCustomAttributeIndex',
  full_name='google.ads.googleads.v0.enums.ListingCustomAttributeIndexEnum.ListingCustomAttributeIndex',
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
      name='CUSTOM_ATTRIBUTE_0', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ATTRIBUTE_1', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ATTRIBUTE_2', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ATTRIBUTE_3', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM_ATTRIBUTE_4', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=144,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX)


_LISTINGCUSTOMATTRIBUTEINDEXENUM = _descriptor.Descriptor(
  name='ListingCustomAttributeIndexEnum',
  full_name='google.ads.googleads.v0.enums.ListingCustomAttributeIndexEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=323,
)

_LISTINGCUSTOMATTRIBUTEINDEXENUM_LISTINGCUSTOMATTRIBUTEINDEX.containing_type = _LISTINGCUSTOMATTRIBUTEINDEXENUM
DESCRIPTOR.message_types_by_name['ListingCustomAttributeIndexEnum'] = _LISTINGCUSTOMATTRIBUTEINDEXENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListingCustomAttributeIndexEnum = _reflection.GeneratedProtocolMessageType('ListingCustomAttributeIndexEnum', (_message.Message,), dict(
  DESCRIPTOR = _LISTINGCUSTOMATTRIBUTEINDEXENUM,
  __module__ = 'google.ads.googleads_v0.proto.enums.listing_custom_attribute_index_pb2'
  ,
  __doc__ = """Container for enum describing the index of the listing custom attribute.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.ListingCustomAttributeIndexEnum)
  ))
_sym_db.RegisterMessage(ListingCustomAttributeIndexEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB ListingCustomAttributeIndexProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
