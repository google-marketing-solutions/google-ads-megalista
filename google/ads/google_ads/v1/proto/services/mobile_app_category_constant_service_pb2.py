# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v1/proto/services/mobile_app_category_constant_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v1.proto.resources import mobile_app_category_constant_pb2 as google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v1/proto/services/mobile_app_category_constant_service.proto',
  package='google.ads.googleads.v1.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v1.servicesB%MobileAppCategoryConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V1.Services\312\002 Google\\Ads\\GoogleAds\\V1\\Services\352\002$Google::Ads::GoogleAds::V1::Services'),
  serialized_pb=_b('\nQgoogle/ads/googleads_v1/proto/services/mobile_app_category_constant_service.proto\x12 google.ads.googleads.v1.services\x1aJgoogle/ads/googleads_v1/proto/resources/mobile_app_category_constant.proto\x1a\x1cgoogle/api/annotations.proto\"<\n#GetMobileAppCategoryConstantRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x82\x02\n MobileAppCategoryConstantService\x12\xdd\x01\n\x1cGetMobileAppCategoryConstant\x12\x45.google.ads.googleads.v1.services.GetMobileAppCategoryConstantRequest\x1a<.google.ads.googleads.v1.resources.MobileAppCategoryConstant\"8\x82\xd3\xe4\x93\x02\x32\x12\x30/v1/{resource_name=mobileAppCategoryConstants/*}B\x8c\x02\n$com.google.ads.googleads.v1.servicesB%MobileAppCategoryConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v1/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V1.Services\xca\x02 Google\\Ads\\GoogleAds\\V1\\Services\xea\x02$Google::Ads::GoogleAds::V1::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_GETMOBILEAPPCATEGORYCONSTANTREQUEST = _descriptor.Descriptor(
  name='GetMobileAppCategoryConstantRequest',
  full_name='google.ads.googleads.v1.services.GetMobileAppCategoryConstantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v1.services.GetMobileAppCategoryConstantRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=225,
  serialized_end=285,
)

DESCRIPTOR.message_types_by_name['GetMobileAppCategoryConstantRequest'] = _GETMOBILEAPPCATEGORYCONSTANTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetMobileAppCategoryConstantRequest = _reflection.GeneratedProtocolMessageType('GetMobileAppCategoryConstantRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMOBILEAPPCATEGORYCONSTANTREQUEST,
  __module__ = 'google.ads.googleads_v1.proto.services.mobile_app_category_constant_service_pb2'
  ,
  __doc__ = """Request message for
  [MobileAppCategoryConstantService.GetMobileAppCategoryConstant][google.ads.googleads.v1.services.MobileAppCategoryConstantService.GetMobileAppCategoryConstant].
  
  
  Attributes:
      resource_name:
          Resource name of the mobile app category constant to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v1.services.GetMobileAppCategoryConstantRequest)
  ))
_sym_db.RegisterMessage(GetMobileAppCategoryConstantRequest)


DESCRIPTOR._options = None

_MOBILEAPPCATEGORYCONSTANTSERVICE = _descriptor.ServiceDescriptor(
  name='MobileAppCategoryConstantService',
  full_name='google.ads.googleads.v1.services.MobileAppCategoryConstantService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=288,
  serialized_end=546,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMobileAppCategoryConstant',
    full_name='google.ads.googleads.v1.services.MobileAppCategoryConstantService.GetMobileAppCategoryConstant',
    index=0,
    containing_service=None,
    input_type=_GETMOBILEAPPCATEGORYCONSTANTREQUEST,
    output_type=google_dot_ads_dot_googleads__v1_dot_proto_dot_resources_dot_mobile__app__category__constant__pb2._MOBILEAPPCATEGORYCONSTANT,
    serialized_options=_b('\202\323\344\223\0022\0220/v1/{resource_name=mobileAppCategoryConstants/*}'),
  ),
])
_sym_db.RegisterServiceDescriptor(_MOBILEAPPCATEGORYCONSTANTSERVICE)

DESCRIPTOR.services_by_name['MobileAppCategoryConstantService'] = _MOBILEAPPCATEGORYCONSTANTSERVICE

# @@protoc_insertion_point(module_scope)
