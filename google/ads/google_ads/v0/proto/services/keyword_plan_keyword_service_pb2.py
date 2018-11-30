# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/keyword_plan_keyword_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import keyword_plan_keyword_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__plan__keyword__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/keyword_plan_keyword_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\nIgoogle/ads/googleads_v0/proto/services/keyword_plan_keyword_service.proto\x12 google.ads.googleads.v0.services\x1a\x42google/ads/googleads_v0/proto/resources/keyword_plan_keyword.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"5\n\x1cGetKeywordPlanKeywordRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\x8a\x01\n MutateKeywordPlanKeywordsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12Q\n\noperations\x18\x02 \x03(\x0b\x32=.google.ads.googleads.v0.services.KeywordPlanKeywordOperation\"\xff\x01\n\x1bKeywordPlanKeywordOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12G\n\x06\x63reate\x18\x01 \x01(\x0b\x32\x35.google.ads.googleads.v0.resources.KeywordPlanKeywordH\x00\x12G\n\x06update\x18\x02 \x01(\x0b\x32\x35.google.ads.googleads.v0.resources.KeywordPlanKeywordH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"v\n!MutateKeywordPlanKeywordsResponse\x12Q\n\x07results\x18\x02 \x03(\x0b\x32@.google.ads.googleads.v0.services.MutateKeywordPlanKeywordResult\"7\n\x1eMutateKeywordPlanKeywordResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xd7\x03\n\x19KeywordPlanKeywordService\x12\xcd\x01\n\x15GetKeywordPlanKeyword\x12>.google.ads.googleads.v0.services.GetKeywordPlanKeywordRequest\x1a\x35.google.ads.googleads.v0.resources.KeywordPlanKeyword\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/v0/{resource_name=customers/*/keywordPlanKeywords/*}\x12\xe9\x01\n\x19MutateKeywordPlanKeywords\x12\x42.google.ads.googleads.v0.services.MutateKeywordPlanKeywordsRequest\x1a\x43.google.ads.googleads.v0.services.MutateKeywordPlanKeywordsResponse\"C\x82\xd3\xe4\x93\x02=\"8/v0/customers/{customer_id=*}/keywordPlanKeywords:mutate:\x01*B\xde\x01\n$com.google.ads.googleads.v0.servicesB\x1eKeywordPlanKeywordServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__plan__keyword__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,])




_GETKEYWORDPLANKEYWORDREQUEST = _descriptor.Descriptor(
  name='GetKeywordPlanKeywordRequest',
  full_name='google.ads.googleads.v0.services.GetKeywordPlanKeywordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetKeywordPlanKeywordRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=296,
)


_MUTATEKEYWORDPLANKEYWORDSREQUEST = _descriptor.Descriptor(
  name='MutateKeywordPlanKeywordsRequest',
  full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=437,
)


_KEYWORDPLANKEYWORDOPERATION = _descriptor.Descriptor(
  name='KeywordPlanKeywordOperation',
  full_name='google.ads.googleads.v0.services.KeywordPlanKeywordOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.KeywordPlanKeywordOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.KeywordPlanKeywordOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.KeywordPlanKeywordOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.KeywordPlanKeywordOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.KeywordPlanKeywordOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=440,
  serialized_end=695,
)


_MUTATEKEYWORDPLANKEYWORDSRESPONSE = _descriptor.Descriptor(
  name='MutateKeywordPlanKeywordsResponse',
  full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordsResponse.results', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=815,
)


_MUTATEKEYWORDPLANKEYWORDRESULT = _descriptor.Descriptor(
  name='MutateKeywordPlanKeywordResult',
  full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateKeywordPlanKeywordResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=817,
  serialized_end=872,
)

_MUTATEKEYWORDPLANKEYWORDSREQUEST.fields_by_name['operations'].message_type = _KEYWORDPLANKEYWORDOPERATION
_KEYWORDPLANKEYWORDOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_KEYWORDPLANKEYWORDOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__plan__keyword__pb2._KEYWORDPLANKEYWORD
_KEYWORDPLANKEYWORDOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__plan__keyword__pb2._KEYWORDPLANKEYWORD
_KEYWORDPLANKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANKEYWORDOPERATION.fields_by_name['create'])
_KEYWORDPLANKEYWORDOPERATION.fields_by_name['create'].containing_oneof = _KEYWORDPLANKEYWORDOPERATION.oneofs_by_name['operation']
_KEYWORDPLANKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANKEYWORDOPERATION.fields_by_name['update'])
_KEYWORDPLANKEYWORDOPERATION.fields_by_name['update'].containing_oneof = _KEYWORDPLANKEYWORDOPERATION.oneofs_by_name['operation']
_KEYWORDPLANKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANKEYWORDOPERATION.fields_by_name['remove'])
_KEYWORDPLANKEYWORDOPERATION.fields_by_name['remove'].containing_oneof = _KEYWORDPLANKEYWORDOPERATION.oneofs_by_name['operation']
_MUTATEKEYWORDPLANKEYWORDSRESPONSE.fields_by_name['results'].message_type = _MUTATEKEYWORDPLANKEYWORDRESULT
DESCRIPTOR.message_types_by_name['GetKeywordPlanKeywordRequest'] = _GETKEYWORDPLANKEYWORDREQUEST
DESCRIPTOR.message_types_by_name['MutateKeywordPlanKeywordsRequest'] = _MUTATEKEYWORDPLANKEYWORDSREQUEST
DESCRIPTOR.message_types_by_name['KeywordPlanKeywordOperation'] = _KEYWORDPLANKEYWORDOPERATION
DESCRIPTOR.message_types_by_name['MutateKeywordPlanKeywordsResponse'] = _MUTATEKEYWORDPLANKEYWORDSRESPONSE
DESCRIPTOR.message_types_by_name['MutateKeywordPlanKeywordResult'] = _MUTATEKEYWORDPLANKEYWORDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKeywordPlanKeywordRequest = _reflection.GeneratedProtocolMessageType('GetKeywordPlanKeywordRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETKEYWORDPLANKEYWORDREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.keyword_plan_keyword_service_pb2'
  ,
  __doc__ = """Request message for
  [KeywordPlanKeywordService.GetKeywordPlanKeyword][google.ads.googleads.v0.services.KeywordPlanKeywordService.GetKeywordPlanKeyword].
  
  
  Attributes:
      resource_name:
          The resource name of the ad group keyword to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetKeywordPlanKeywordRequest)
  ))
_sym_db.RegisterMessage(GetKeywordPlanKeywordRequest)

MutateKeywordPlanKeywordsRequest = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanKeywordsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANKEYWORDSREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.keyword_plan_keyword_service_pb2'
  ,
  __doc__ = """Request message for
  [KeywordPlanKeywordService.MutateKeywordPlanKeywords][google.ads.googleads.v0.services.KeywordPlanKeywordService.MutateKeywordPlanKeywords].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose Keyword Plan keywords are being
          modified.
      operations:
          The list of operations to perform on individual Keyword Plan
          keywords.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateKeywordPlanKeywordsRequest)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanKeywordsRequest)

KeywordPlanKeywordOperation = _reflection.GeneratedProtocolMessageType('KeywordPlanKeywordOperation', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANKEYWORDOPERATION,
  __module__ = 'google.ads.google_ads.v0.proto.services.keyword_plan_keyword_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a Keyword Plan keyword.
  
  
  Attributes:
      update_mask:
          The FieldMask that determines which resource fields are
          modified in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          Keyword Plan ad group keyword.
      update:
          Update operation: The Keyword Plan keyword is expected to have
          a valid resource name.
      remove:
          Remove operation: A resource name for the removed Keyword Plan
          keyword is expected, in this format:  ``customers/{customer_id
          }/keywordPlanKeywords/{kp_ad_group_keyword_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.KeywordPlanKeywordOperation)
  ))
_sym_db.RegisterMessage(KeywordPlanKeywordOperation)

MutateKeywordPlanKeywordsResponse = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanKeywordsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANKEYWORDSRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.keyword_plan_keyword_service_pb2'
  ,
  __doc__ = """Response message for a Keyword Plan keyword mutate.
  
  
  Attributes:
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateKeywordPlanKeywordsResponse)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanKeywordsResponse)

MutateKeywordPlanKeywordResult = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanKeywordResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANKEYWORDRESULT,
  __module__ = 'google.ads.google_ads.v0.proto.services.keyword_plan_keyword_service_pb2'
  ,
  __doc__ = """The result for the Keyword Plan keyword mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateKeywordPlanKeywordResult)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanKeywordResult)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\036KeywordPlanKeywordServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_KEYWORDPLANKEYWORDSERVICE = _descriptor.ServiceDescriptor(
  name='KeywordPlanKeywordService',
  full_name='google.ads.googleads.v0.services.KeywordPlanKeywordService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=875,
  serialized_end=1346,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetKeywordPlanKeyword',
    full_name='google.ads.googleads.v0.services.KeywordPlanKeywordService.GetKeywordPlanKeyword',
    index=0,
    containing_service=None,
    input_type=_GETKEYWORDPLANKEYWORDREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_keyword__plan__keyword__pb2._KEYWORDPLANKEYWORD,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0027\0225/v0/{resource_name=customers/*/keywordPlanKeywords/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateKeywordPlanKeywords',
    full_name='google.ads.googleads.v0.services.KeywordPlanKeywordService.MutateKeywordPlanKeywords',
    index=1,
    containing_service=None,
    input_type=_MUTATEKEYWORDPLANKEYWORDSREQUEST,
    output_type=_MUTATEKEYWORDPLANKEYWORDSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002=\"8/v0/customers/{customer_id=*}/keywordPlanKeywords:mutate:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYWORDPLANKEYWORDSERVICE)

DESCRIPTOR.services_by_name['KeywordPlanKeywordService'] = _KEYWORDPLANKEYWORDSERVICE

# @@protoc_insertion_point(module_scope)
