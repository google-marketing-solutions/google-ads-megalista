# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/services/customer_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.resources import customer_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/services/customer_service.proto',
  package='google.ads.googleads.v0.services',
  syntax='proto3',
  serialized_pb=_b('\n=google/ads/googleads_v0/proto/services/customer_service.proto\x12 google.ads.googleads.v0.services\x1a\x36google/ads/googleads_v0/proto/resources/customer.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto\"+\n\x12GetCustomerRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\"t\n\x15MutateCustomerRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x46\n\toperation\x18\x04 \x01(\x0b\x32\x33.google.ads.googleads.v0.services.CustomerOperation\"x\n\x1b\x43reateCustomerClientRequest\x12\x13\n\x0b\x63ustomer_id\x18\x01 \x01(\t\x12\x44\n\x0f\x63ustomer_client\x18\x02 \x01(\x0b\x32+.google.ads.googleads.v0.resources.Customer\"\x81\x01\n\x11\x43ustomerOperation\x12;\n\x06update\x18\x01 \x01(\x0b\x32+.google.ads.googleads.v0.resources.Customer\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"5\n\x1c\x43reateCustomerClientResponse\x12\x15\n\rresource_name\x18\x02 \x01(\t\"`\n\x16MutateCustomerResponse\x12\x46\n\x06result\x18\x02 \x01(\x0b\x32\x36.google.ads.googleads.v0.services.MutateCustomerResult\"-\n\x14MutateCustomerResult\x12\x15\n\rresource_name\x18\x01 \x01(\t\" \n\x1eListAccessibleCustomersRequest\"9\n\x1fListAccessibleCustomersResponse\x12\x16\n\x0eresource_names\x18\x01 \x03(\t2\x8b\x06\n\x0f\x43ustomerService\x12\x99\x01\n\x0bGetCustomer\x12\x34.google.ads.googleads.v0.services.GetCustomerRequest\x1a+.google.ads.googleads.v0.resources.Customer\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v0/{resource_name=customers/*}\x12\xb4\x01\n\x0eMutateCustomer\x12\x37.google.ads.googleads.v0.services.MutateCustomerRequest\x1a\x38.google.ads.googleads.v0.services.MutateCustomerResponse\"/\x82\xd3\xe4\x93\x02)\"$/v0/customers/{customer_id=*}:mutate:\x01*\x12\xcd\x01\n\x17ListAccessibleCustomers\x12@.google.ads.googleads.v0.services.ListAccessibleCustomersRequest\x1a\x41.google.ads.googleads.v0.services.ListAccessibleCustomersResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v0/customers:listAccessibleCustomers\x12\xd4\x01\n\x14\x43reateCustomerClient\x12=.google.ads.googleads.v0.services.CreateCustomerClientRequest\x1a>.google.ads.googleads.v0.services.CreateCustomerClientResponse\"=\x82\xd3\xe4\x93\x02\x37\"2/v0/customers/{customer_id=*}:createCustomerClient:\x01*B\xd4\x01\n$com.google.ads.googleads.v0.servicesB\x14\x43ustomerServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V0.Services\xca\x02 Google\\Ads\\GoogleAds\\V0\\Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_GETCUSTOMERREQUEST = _descriptor.Descriptor(
  name='GetCustomerRequest',
  full_name='google.ads.googleads.v0.services.GetCustomerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.GetCustomerRequest.resource_name', index=0,
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
  serialized_start=251,
  serialized_end=294,
)


_MUTATECUSTOMERREQUEST = _descriptor.Descriptor(
  name='MutateCustomerRequest',
  full_name='google.ads.googleads.v0.services.MutateCustomerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.MutateCustomerRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.ads.googleads.v0.services.MutateCustomerRequest.operation', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=296,
  serialized_end=412,
)


_CREATECUSTOMERCLIENTREQUEST = _descriptor.Descriptor(
  name='CreateCustomerClientRequest',
  full_name='google.ads.googleads.v0.services.CreateCustomerClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v0.services.CreateCustomerClientRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='customer_client', full_name='google.ads.googleads.v0.services.CreateCustomerClientRequest.customer_client', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=414,
  serialized_end=534,
)


_CUSTOMEROPERATION = _descriptor.Descriptor(
  name='CustomerOperation',
  full_name='google.ads.googleads.v0.services.CustomerOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v0.services.CustomerOperation.update', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v0.services.CustomerOperation.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=537,
  serialized_end=666,
)


_CREATECUSTOMERCLIENTRESPONSE = _descriptor.Descriptor(
  name='CreateCustomerClientResponse',
  full_name='google.ads.googleads.v0.services.CreateCustomerClientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.CreateCustomerClientResponse.resource_name', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=668,
  serialized_end=721,
)


_MUTATECUSTOMERRESPONSE = _descriptor.Descriptor(
  name='MutateCustomerResponse',
  full_name='google.ads.googleads.v0.services.MutateCustomerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='google.ads.googleads.v0.services.MutateCustomerResponse.result', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=723,
  serialized_end=819,
)


_MUTATECUSTOMERRESULT = _descriptor.Descriptor(
  name='MutateCustomerResult',
  full_name='google.ads.googleads.v0.services.MutateCustomerResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.services.MutateCustomerResult.resource_name', index=0,
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
  serialized_start=821,
  serialized_end=866,
)


_LISTACCESSIBLECUSTOMERSREQUEST = _descriptor.Descriptor(
  name='ListAccessibleCustomersRequest',
  full_name='google.ads.googleads.v0.services.ListAccessibleCustomersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=868,
  serialized_end=900,
)


_LISTACCESSIBLECUSTOMERSRESPONSE = _descriptor.Descriptor(
  name='ListAccessibleCustomersResponse',
  full_name='google.ads.googleads.v0.services.ListAccessibleCustomersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_names', full_name='google.ads.googleads.v0.services.ListAccessibleCustomersResponse.resource_names', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=902,
  serialized_end=959,
)

_MUTATECUSTOMERREQUEST.fields_by_name['operation'].message_type = _CUSTOMEROPERATION
_CREATECUSTOMERCLIENTREQUEST.fields_by_name['customer_client'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2._CUSTOMER
_CUSTOMEROPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2._CUSTOMER
_CUSTOMEROPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_MUTATECUSTOMERRESPONSE.fields_by_name['result'].message_type = _MUTATECUSTOMERRESULT
DESCRIPTOR.message_types_by_name['GetCustomerRequest'] = _GETCUSTOMERREQUEST
DESCRIPTOR.message_types_by_name['MutateCustomerRequest'] = _MUTATECUSTOMERREQUEST
DESCRIPTOR.message_types_by_name['CreateCustomerClientRequest'] = _CREATECUSTOMERCLIENTREQUEST
DESCRIPTOR.message_types_by_name['CustomerOperation'] = _CUSTOMEROPERATION
DESCRIPTOR.message_types_by_name['CreateCustomerClientResponse'] = _CREATECUSTOMERCLIENTRESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomerResponse'] = _MUTATECUSTOMERRESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomerResult'] = _MUTATECUSTOMERRESULT
DESCRIPTOR.message_types_by_name['ListAccessibleCustomersRequest'] = _LISTACCESSIBLECUSTOMERSREQUEST
DESCRIPTOR.message_types_by_name['ListAccessibleCustomersResponse'] = _LISTACCESSIBLECUSTOMERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomerRequest = _reflection.GeneratedProtocolMessageType('GetCustomerRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETCUSTOMERREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerService.GetCustomer][google.ads.googleads.v0.services.CustomerService.GetCustomer].
  
  
  Attributes:
      resource_name:
          The resource name of the customer to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.GetCustomerRequest)
  ))
_sym_db.RegisterMessage(GetCustomerRequest)

MutateCustomerRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECUSTOMERREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerService.MutateCustomer][google.ads.googleads.v0.services.CustomerService.MutateCustomer].
  
  
  Attributes:
      customer_id:
          The ID of the customer being modified.
      operation:
          The operation to perform on the customer
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCustomerRequest)
  ))
_sym_db.RegisterMessage(MutateCustomerRequest)

CreateCustomerClientRequest = _reflection.GeneratedProtocolMessageType('CreateCustomerClientRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATECUSTOMERCLIENTREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerService.CreateCustomerClient][google.ads.googleads.v0.services.CustomerService.CreateCustomerClient].
  
  
  Attributes:
      customer_id:
          The ID of the Manager under whom client customer is being
          created.
      customer_client:
          The new client customer to create. The resource name on this
          customer will be ignored.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.CreateCustomerClientRequest)
  ))
_sym_db.RegisterMessage(CreateCustomerClientRequest)

CustomerOperation = _reflection.GeneratedProtocolMessageType('CustomerOperation', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMEROPERATION,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """A single update on a customer.
  
  
  Attributes:
      update:
          Mutate operation. Only updates are supported for customer.
      update_mask:
          FieldMask that determines which resource fields are modified
          in an update.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.CustomerOperation)
  ))
_sym_db.RegisterMessage(CustomerOperation)

CreateCustomerClientResponse = _reflection.GeneratedProtocolMessageType('CreateCustomerClientResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATECUSTOMERCLIENTRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Response message for CreateCustomerClient mutate.
  
  
  Attributes:
      resource_name:
          The resource name of the newly created customer client.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.CreateCustomerClientResponse)
  ))
_sym_db.RegisterMessage(CreateCustomerClientResponse)

MutateCustomerResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECUSTOMERRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Response message for customer mutate.
  
  
  Attributes:
      result:
          Result for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCustomerResponse)
  ))
_sym_db.RegisterMessage(MutateCustomerResponse)

MutateCustomerResult = _reflection.GeneratedProtocolMessageType('MutateCustomerResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATECUSTOMERRESULT,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """The result for the customer mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.MutateCustomerResult)
  ))
_sym_db.RegisterMessage(MutateCustomerResult)

ListAccessibleCustomersRequest = _reflection.GeneratedProtocolMessageType('ListAccessibleCustomersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTACCESSIBLECUSTOMERSREQUEST,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Request message for
  [CustomerService.ListAccessibleCustomers][google.ads.googleads.v0.services.CustomerService.ListAccessibleCustomers].
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ListAccessibleCustomersRequest)
  ))
_sym_db.RegisterMessage(ListAccessibleCustomersRequest)

ListAccessibleCustomersResponse = _reflection.GeneratedProtocolMessageType('ListAccessibleCustomersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTACCESSIBLECUSTOMERSRESPONSE,
  __module__ = 'google.ads.google_ads.v0.proto.services.customer_service_pb2'
  ,
  __doc__ = """Response message for
  [CustomerService.ListAccessibleCustomers][google.ads.googleads.v0.services.CustomerService.ListAccessibleCustomers].
  
  
  Attributes:
      resource_names:
          Resource name of customers directly accessible by the user
          authenticating the call.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.services.ListAccessibleCustomersResponse)
  ))
_sym_db.RegisterMessage(ListAccessibleCustomersResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n$com.google.ads.googleads.v0.servicesB\024CustomerServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v0/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V0.Services\312\002 Google\\Ads\\GoogleAds\\V0\\Services'))

_CUSTOMERSERVICE = _descriptor.ServiceDescriptor(
  name='CustomerService',
  full_name='google.ads.googleads.v0.services.CustomerService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=962,
  serialized_end=1741,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomer',
    full_name='google.ads.googleads.v0.services.CustomerService.GetCustomer',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMERREQUEST,
    output_type=google_dot_ads_dot_googleads__v0_dot_proto_dot_resources_dot_customer__pb2._CUSTOMER,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002!\022\037/v0/{resource_name=customers/*}')),
  ),
  _descriptor.MethodDescriptor(
    name='MutateCustomer',
    full_name='google.ads.googleads.v0.services.CustomerService.MutateCustomer',
    index=1,
    containing_service=None,
    input_type=_MUTATECUSTOMERREQUEST,
    output_type=_MUTATECUSTOMERRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002)\"$/v0/customers/{customer_id=*}:mutate:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='ListAccessibleCustomers',
    full_name='google.ads.googleads.v0.services.CustomerService.ListAccessibleCustomers',
    index=2,
    containing_service=None,
    input_type=_LISTACCESSIBLECUSTOMERSREQUEST,
    output_type=_LISTACCESSIBLECUSTOMERSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\'\022%/v0/customers:listAccessibleCustomers')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateCustomerClient',
    full_name='google.ads.googleads.v0.services.CustomerService.CreateCustomerClient',
    index=3,
    containing_service=None,
    input_type=_CREATECUSTOMERCLIENTREQUEST,
    output_type=_CREATECUSTOMERCLIENTRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\0027\"2/v0/customers/{customer_id=*}:createCustomerClient:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERSERVICE)

DESCRIPTOR.services_by_name['CustomerService'] = _CUSTOMERSERVICE

# @@protoc_insertion_point(module_scope)
