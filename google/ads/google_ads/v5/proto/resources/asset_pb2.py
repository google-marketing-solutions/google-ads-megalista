# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v5/proto/resources/asset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v5.proto.common import asset_types_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2
from google.ads.google_ads.v5.proto.enums import asset_type_pb2 as google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_asset__type__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v5/proto/resources/asset.proto',
  package='google.ads.googleads.v5.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v5.resourcesB\nAssetProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V5.Resources\312\002!Google\\Ads\\GoogleAds\\V5\\Resources\352\002%Google::Ads::GoogleAds::V5::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/ads/googleads_v5/proto/resources/asset.proto\x12!google.ads.googleads.v5.resources\x1a\x36google/ads/googleads_v5/proto/common/asset_types.proto\x1a\x34google/ads/googleads_v5/proto/enums/asset_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xaf\x05\n\x05\x41sset\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0\x41\x05\xfa\x41 \n\x1egoogleads.googleapis.com/Asset\x12\x14\n\x02id\x18\x0b \x01(\x03\x42\x03\xe0\x41\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x0c \x01(\tH\x02\x88\x01\x01\x12I\n\x04type\x18\x04 \x01(\x0e\x32\x36.google.ads.googleads.v5.enums.AssetTypeEnum.AssetTypeB\x03\xe0\x41\x03\x12U\n\x13youtube_video_asset\x18\x05 \x01(\x0b\x32\x31.google.ads.googleads.v5.common.YoutubeVideoAssetB\x03\xe0\x41\x05H\x00\x12S\n\x12media_bundle_asset\x18\x06 \x01(\x0b\x32\x30.google.ads.googleads.v5.common.MediaBundleAssetB\x03\xe0\x41\x05H\x00\x12\x46\n\x0bimage_asset\x18\x07 \x01(\x0b\x32*.google.ads.googleads.v5.common.ImageAssetB\x03\xe0\x41\x03H\x00\x12\x44\n\ntext_asset\x18\x08 \x01(\x0b\x32).google.ads.googleads.v5.common.TextAssetB\x03\xe0\x41\x03H\x00\x12Q\n\x14\x62ook_on_google_asset\x18\n \x01(\x0b\x32\x31.google.ads.googleads.v5.common.BookOnGoogleAssetH\x00:H\xea\x41\x45\n\x1egoogleads.googleapis.com/Asset\x12#customers/{customer}/assets/{asset}B\x0c\n\nasset_dataB\x05\n\x03_idB\x07\n\x05_nameB\xf7\x01\n%com.google.ads.googleads.v5.resourcesB\nAssetProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v5/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V5.Resources\xca\x02!Google\\Ads\\GoogleAds\\V5\\Resources\xea\x02%Google::Ads::GoogleAds::V5::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_asset__type__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ASSET = _descriptor.Descriptor(
  name='Asset',
  full_name='google.ads.googleads.v5.resources.Asset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v5.resources.Asset.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005\372A \n\036googleads.googleapis.com/Asset', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v5.resources.Asset.id', index=1,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v5.resources.Asset.name', index=2,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v5.resources.Asset.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='youtube_video_asset', full_name='google.ads.googleads.v5.resources.Asset.youtube_video_asset', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='media_bundle_asset', full_name='google.ads.googleads.v5.resources.Asset.media_bundle_asset', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\005', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='image_asset', full_name='google.ads.googleads.v5.resources.Asset.image_asset', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_asset', full_name='google.ads.googleads.v5.resources.Asset.text_asset', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\340A\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book_on_google_asset', full_name='google.ads.googleads.v5.resources.Asset.book_on_google_asset', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352AE\n\036googleads.googleapis.com/Asset\022#customers/{customer}/assets/{asset}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='asset_data', full_name='google.ads.googleads.v5.resources.Asset.asset_data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v5.resources.Asset._id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v5.resources.Asset._name',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=291,
  serialized_end=978,
)

_ASSET.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_enums_dot_asset__type__pb2._ASSETTYPEENUM_ASSETTYPE
_ASSET.fields_by_name['youtube_video_asset'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2._YOUTUBEVIDEOASSET
_ASSET.fields_by_name['media_bundle_asset'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2._MEDIABUNDLEASSET
_ASSET.fields_by_name['image_asset'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2._IMAGEASSET
_ASSET.fields_by_name['text_asset'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2._TEXTASSET
_ASSET.fields_by_name['book_on_google_asset'].message_type = google_dot_ads_dot_googleads__v5_dot_proto_dot_common_dot_asset__types__pb2._BOOKONGOOGLEASSET
_ASSET.oneofs_by_name['asset_data'].fields.append(
  _ASSET.fields_by_name['youtube_video_asset'])
_ASSET.fields_by_name['youtube_video_asset'].containing_oneof = _ASSET.oneofs_by_name['asset_data']
_ASSET.oneofs_by_name['asset_data'].fields.append(
  _ASSET.fields_by_name['media_bundle_asset'])
_ASSET.fields_by_name['media_bundle_asset'].containing_oneof = _ASSET.oneofs_by_name['asset_data']
_ASSET.oneofs_by_name['asset_data'].fields.append(
  _ASSET.fields_by_name['image_asset'])
_ASSET.fields_by_name['image_asset'].containing_oneof = _ASSET.oneofs_by_name['asset_data']
_ASSET.oneofs_by_name['asset_data'].fields.append(
  _ASSET.fields_by_name['text_asset'])
_ASSET.fields_by_name['text_asset'].containing_oneof = _ASSET.oneofs_by_name['asset_data']
_ASSET.oneofs_by_name['asset_data'].fields.append(
  _ASSET.fields_by_name['book_on_google_asset'])
_ASSET.fields_by_name['book_on_google_asset'].containing_oneof = _ASSET.oneofs_by_name['asset_data']
_ASSET.oneofs_by_name['_id'].fields.append(
  _ASSET.fields_by_name['id'])
_ASSET.fields_by_name['id'].containing_oneof = _ASSET.oneofs_by_name['_id']
_ASSET.oneofs_by_name['_name'].fields.append(
  _ASSET.fields_by_name['name'])
_ASSET.fields_by_name['name'].containing_oneof = _ASSET.oneofs_by_name['_name']
DESCRIPTOR.message_types_by_name['Asset'] = _ASSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Asset = _reflection.GeneratedProtocolMessageType('Asset', (_message.Message,), {
  'DESCRIPTOR' : _ASSET,
  '__module__' : 'google.ads.googleads_v5.proto.resources.asset_pb2'
  ,
  '__doc__': """Asset is a part of an ad which can be shared across multiple ads. It
  can be an image (ImageAsset), a video (YoutubeVideoAsset), etc.
  
  Attributes:
      resource_name:
          Immutable. The resource name of the asset. Asset resource
          names have the form:
          ``customers/{customer_id}/assets/{asset_id}``
      id:
          Output only. The ID of the asset.
      name:
          Optional name of the asset.
      type:
          Output only. Type of the asset.
      asset_data:
          The specific type of the asset.
      youtube_video_asset:
          Immutable. A YouTube video asset.
      media_bundle_asset:
          Immutable. A media bundle asset.
      image_asset:
          Output only. An image asset.
      text_asset:
          Output only. A text asset.
      book_on_google_asset:
          A book on google asset.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v5.resources.Asset)
  })
_sym_db.RegisterMessage(Asset)


DESCRIPTOR._options = None
_ASSET.fields_by_name['resource_name']._options = None
_ASSET.fields_by_name['id']._options = None
_ASSET.fields_by_name['type']._options = None
_ASSET.fields_by_name['youtube_video_asset']._options = None
_ASSET.fields_by_name['media_bundle_asset']._options = None
_ASSET.fields_by_name['image_asset']._options = None
_ASSET.fields_by_name['text_asset']._options = None
_ASSET._options = None
# @@protoc_insertion_point(module_scope)
