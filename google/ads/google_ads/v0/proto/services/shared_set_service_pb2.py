# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/shared_set_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import shared_set_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/shared_set_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v0.servicesB\025SharedSetServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services\352\002$Google::Ads::GoogleAds::V0::Services'),
  serialized_pb=_b('\n?google/ads/googleads_v0/proto/services/shared_set_service.proto\x12 google.ads.googleads.v0.services\x1a\x38google/ads/googleads_v0/proto/resources/shared_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\",\n\x13GetSharedSetRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"\xa8\x01\n\x17MutateSharedSetsRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12H\n\noperations\x18\x02 \x03(\x0b\x32\x34.google.ads.googleads.v0.services.SharedSetOperation\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\xe4\x01\n\x12SharedSetOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12>\n\x06\x63reate\x18\x01 \x01(\x0b\x32,.google.ads.googleads.v0.resources.SharedSetH\x00\x12>\n\x06update\x18\x02 \x01(\x0b\x32,.google.ads.googleads.v0.resources.SharedSetH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\x97\x01\n\x18MutateSharedSetsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12H\n\x07results\x18\x02 \x03(\x0b\x32\x37.google.ads.googleads.v0.services.MutateSharedSetResult\".\n\x15MutateSharedSetResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\x86\x03\n\x10SharedSetService\x12\xa9\x01\n\x0cGetSharedSet\x12\x35.google.ads.googleads.v0.services.GetSharedSetRequest\x1a,.google.ads.googleads.v0.resources.SharedSet\"4\x82\xd3\xe4\x93\x02.\x12,/v0/{resource_name=customers/*/sharedSets/*}\x12\xc5\x01\n\x10MutateSharedSets\x12\x39.google.ads.googleads.v0.services.MutateSharedSetsRequest\x1a:.google.ads.googleads.v0.services.MutateSharedSetsResponse\":\x82\xd3\xe4\x93\x02\x34\"//v0/customers/{customer_id=*}/sharedSets:mutate:\x01*B\xfc\x01\n$com.google.ads.googleads.v0.servicesB\x15SharedSetServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Services\xea\x02$Google::Ads::GoogleAds::V0::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETSHAREDSETREQUEST = _descriptor.Descriptor(
  name='GetSharedSetRequest',
  full_name='google.ads.googleads.v0.services.GetSharedSetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetSharedSetRequest.resource_name', index=0,
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
  serialized_start=280,
  serialized_end=324,
)


_MUTATESHAREDSETSREQUEST = _descriptor.Descriptor(
  name='MutateSharedSetsRequest',
  full_name='google.ads.googleads.v0.services.MutateSharedSetsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateSharedSetsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v0.services.MutateSharedSetsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v0.services.MutateSharedSetsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v0.services.MutateSharedSetsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=327,
  serialized_end=495,
)


_SHAREDSETOPERATION = _descriptor.Descriptor(
  name='SharedSetOperation',
  full_name='google.ads.googleads.v0.services.SharedSetOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.SharedSetOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v0.services.SharedSetOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.SharedSetOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v0.services.SharedSetOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.SharedSetOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=498,
  serialized_end=726,
)


_MUTATESHAREDSETSRESPONSE = _descriptor.Descriptor(
  name='MutateSharedSetsResponse',
  full_name='google.ads.googleads.v0.services.MutateSharedSetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v0.services.MutateSharedSetsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v0.services.MutateSharedSetsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=729,
  serialized_end=880,
)


_MUTATESHAREDSETRESULT = _descriptor.Descriptor(
  name='MutateSharedSetResult',
  full_name='google.ads.googleads.v0.services.MutateSharedSetResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateSharedSetResult.resource_name', index=0,
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
  serialized_start=882,
  serialized_end=928,
)

_MUTATESHAREDSETSREQUEST.fields_by_name['operations'].message_type = _SHAREDSETOPERATION
_SHAREDSETOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_SHAREDSETOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2._SHAREDSET
_SHAREDSETOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2._SHAREDSET
_SHAREDSETOPERATION.oneofs_by_name['operation'].fields.append(
  _SHAREDSETOPERATION.fields_by_name['create'])
_SHAREDSETOPERATION.fields_by_name['create'].containing_oneof = _SHAREDSETOPERATION.oneofs_by_name['operation']
_SHAREDSETOPERATION.oneofs_by_name['operation'].fields.append(
  _SHAREDSETOPERATION.fields_by_name['update'])
_SHAREDSETOPERATION.fields_by_name['update'].containing_oneof = _SHAREDSETOPERATION.oneofs_by_name['operation']
_SHAREDSETOPERATION.oneofs_by_name['operation'].fields.append(
  _SHAREDSETOPERATION.fields_by_name['remove'])
_SHAREDSETOPERATION.fields_by_name['remove'].containing_oneof = _SHAREDSETOPERATION.oneofs_by_name['operation']
_MUTATESHAREDSETSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATESHAREDSETSRESPONSE.fields_by_name['results'].message_type = _MUTATESHAREDSETRESULT
DESCRIPTOR.message_types_by_name['GetSharedSetRequest'] = _GETSHAREDSETREQUEST
DESCRIPTOR.message_types_by_name['MutateSharedSetsRequest'] = _MUTATESHAREDSETSREQUEST
DESCRIPTOR.message_types_by_name['SharedSetOperation'] = _SHAREDSETOPERATION
DESCRIPTOR.message_types_by_name['MutateSharedSetsResponse'] = _MUTATESHAREDSETSRESPONSE
DESCRIPTOR.message_types_by_name['MutateSharedSetResult'] = _MUTATESHAREDSETRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetSharedSetRequest = _reflection.GeneratedProtocolMessageType('GetSharedSetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSHAREDSETREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_set_service_pb2'
  ,
  __doc__ = """Request message for
  [SharedSetService.GetSharedSet][google.ads.googleads.v0.services.SharedSetService.GetSharedSet].
  
  
  Attributes:
      resource_name:
          The resource name of the shared set to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetSharedSetRequest)
  ))
_sym_db.RegisterMessage(GetSharedSetRequest)

MutateSharedSetsRequest = _reflection.GeneratedProtocolMessageType('MutateSharedSetsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATESHAREDSETSREQUEST,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_set_service_pb2'
  ,
  __doc__ = """Request message for
  [SharedSetService.MutateSharedSets][google.ads.googleads.v0.services.SharedSetService.MutateSharedSets].
  
  
  Attributes:
      customer_id:
          The ID of the customer whose shared sets are being modified.
      operations:
          The list of operations to perform on individual shared sets.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateSharedSetsRequest)
  ))
_sym_db.RegisterMessage(MutateSharedSetsRequest)

SharedSetOperation = _reflection.GeneratedProtocolMessageType('SharedSetOperation', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSETOPERATION,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_set_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on an shared set.
  
  
  Attributes:
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          shared set.
      update:
          Update operation: The shared set is expected to have a valid
          resource name.
      remove:
          Remove operation: A resource name for the removed shared set
          is expected, in this format:
          ``customers/{customer_id}/sharedSets/{shared_set_id}``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.SharedSetOperation)
  ))
_sym_db.RegisterMessage(SharedSetOperation)

MutateSharedSetsResponse = _reflection.GeneratedProtocolMessageType('MutateSharedSetsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATESHAREDSETSRESPONSE,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_set_service_pb2'
  ,
  __doc__ = """Response message for a shared set mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateSharedSetsResponse)
  ))
_sym_db.RegisterMessage(MutateSharedSetsResponse)

MutateSharedSetResult = _reflection.GeneratedProtocolMessageType('MutateSharedSetResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATESHAREDSETRESULT,
  __module__ = 'google.ads.googleads_v0.proto.services.shared_set_service_pb2'
  ,
  __doc__ = """The result for the shared set mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateSharedSetResult)
  ))
_sym_db.RegisterMessage(MutateSharedSetResult)


DESCRIPTOR._options = None

_SHAREDSETSERVICE = _descriptor.ServiceDescriptor(
  name='SharedSetService',
  full_name='google.ads.googleads.v0.services.SharedSetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=931,
  serialized_end=1321,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSharedSet',
    full_name='google.ads.googleads.v0.services.SharedSetService.GetSharedSet',
    index=0,
    containing_service=None,
    input_type=_GETSHAREDSETREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_shared__set__pb2._SHAREDSET,
    serialized_options=_b('\202\323\344\223\002.\022,/v0/{resource_name=customers/*/sharedSets/*}'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateSharedSets',
    full_name='google.ads.googleads.v0.services.SharedSetService.MutateSharedSets',
    index=1,
    containing_service=None,
    input_type=_MUTATESHAREDSETSREQUEST,
    output_type=_MUTATESHAREDSETSRESPONSE,
    serialized_options=_b('\202\323\344\223\0024\"//v0/customers/{customer_id=*}/sharedSets:mutate:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_SHAREDSETSERVICE)

DESCRIPTOR.services_by_name['SharedSetService'] = _SHAREDSETSERVICE

# @@protoc_insertion_point(module_scope)
