# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/policy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.enums import policy_topic_entry_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_policy__topic__entry__type__pb2
from google.ads.google_ads.v0.proto.enums import policy_topic_evidence_destination_mismatch_url_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_policy__topic__evidence__destination__mismatch__url__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/common/policy.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_pb=_b('\n1google/ads/googleads_v0/proto/common/policy.proto\x12\x1egoogle.ads.googleads.v0.common\x1a\x41google/ads/googleads_v0/proto/enums/policy_topic_entry_type.proto\x1a]google/ads/googleads_v0/proto/enums/policy_topic_evidence_destination_mismatch_url_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\"}\n\x12PolicyViolationKey\x12\x31\n\x0bpolicy_name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0eviolating_text\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"Z\n\x19PolicyValidationParameter\x12=\n\x17ignorable_policy_topics\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\"\xaf\x02\n\x10PolicyTopicEntry\x12+\n\x05topic\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12Z\n\x04type\x18\x02 \x01(\x0e\x32L.google.ads.googleads.v0.enums.PolicyTopicEntryTypeEnum.PolicyTopicEntryType\x12\x46\n\tevidences\x18\x03 \x03(\x0b\x32\x33.google.ads.googleads.v0.common.PolicyTopicEvidence\x12J\n\x0b\x63onstraints\x18\x04 \x03(\x0b\x32\x35.google.ads.googleads.v0.common.PolicyTopicConstraint\"\xfa\x06\n\x13PolicyTopicEvidence\x12\x30\n\thttp_code\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueH\x00\x12W\n\x0cwebsite_list\x18\x03 \x01(\x0b\x32?.google.ads.googleads.v0.common.PolicyTopicEvidence.WebsiteListH\x00\x12Q\n\ttext_list\x18\x04 \x01(\x0b\x32<.google.ads.googleads.v0.common.PolicyTopicEvidence.TextListH\x00\x12\x35\n\rlanguage_code\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValueH\x00\x12h\n\x15\x64\x65stination_text_list\x18\x06 \x01(\x0b\x32G.google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationTextListH\x00\x12g\n\x14\x64\x65stination_mismatch\x18\x07 \x01(\x0b\x32G.google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationMismatchH\x00\x1a\x37\n\x08TextList\x12+\n\x05texts\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x1a=\n\x0bWebsiteList\x12.\n\x08websites\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x1aN\n\x13\x44\x65stinationTextList\x12\x37\n\x11\x64\x65stination_texts\x18\x01 \x03(\x0b\x32\x1c.google.protobuf.StringValue\x1a\xa9\x01\n\x13\x44\x65stinationMismatch\x12\x91\x01\n\turl_types\x18\x01 \x03(\x0e\x32~.google.ads.googleads.v0.enums.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlTypeB\x07\n\x05value\"\x93\x06\n\x15PolicyTopicConstraint\x12n\n\x17\x63ountry_constraint_list\x18\x01 \x01(\x0b\x32K.google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintListH\x00\x12g\n\x13reseller_constraint\x18\x02 \x01(\x0b\x32H.google.ads.googleads.v0.common.PolicyTopicConstraint.ResellerConstraintH\x00\x12z\n#certificate_missing_in_country_list\x18\x03 \x01(\x0b\x32K.google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintListH\x00\x12\x82\x01\n+certificate_domain_mismatch_in_country_list\x18\x04 \x01(\x0b\x32K.google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintListH\x00\x1a\xb2\x01\n\x15\x43ountryConstraintList\x12=\n\x18total_targeted_countries\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12Z\n\tcountries\x18\x02 \x03(\x0b\x32G.google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraint\x1a\x14\n\x12ResellerConstraint\x1aL\n\x11\x43ountryConstraint\x12\x37\n\x11\x63ountry_criterion\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x07\n\x05valueB\xc1\x01\n\"com.google.ads.googleads.v0.commonB\x0bPolicyProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Commonb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_policy__topic__entry__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_policy__topic__evidence__destination__mismatch__url__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_POLICYVIOLATIONKEY = _descriptor.Descriptor(
  name='PolicyViolationKey',
  full_name='google.ads.googleads.v0.common.PolicyViolationKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_name', full_name='google.ads.googleads.v0.common.PolicyViolationKey.policy_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='violating_text', full_name='google.ads.googleads.v0.common.PolicyViolationKey.violating_text', index=1,
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
  serialized_start=279,
  serialized_end=404,
)


_POLICYVALIDATIONPARAMETER = _descriptor.Descriptor(
  name='PolicyValidationParameter',
  full_name='google.ads.googleads.v0.common.PolicyValidationParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ignorable_policy_topics', full_name='google.ads.googleads.v0.common.PolicyValidationParameter.ignorable_policy_topics', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=406,
  serialized_end=496,
)


_POLICYTOPICENTRY = _descriptor.Descriptor(
  name='PolicyTopicEntry',
  full_name='google.ads.googleads.v0.common.PolicyTopicEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='google.ads.googleads.v0.common.PolicyTopicEntry.topic', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.ads.googleads.v0.common.PolicyTopicEntry.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evidences', full_name='google.ads.googleads.v0.common.PolicyTopicEntry.evidences', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='google.ads.googleads.v0.common.PolicyTopicEntry.constraints', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=499,
  serialized_end=802,
)


_POLICYTOPICEVIDENCE_TEXTLIST = _descriptor.Descriptor(
  name='TextList',
  full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.TextList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='texts', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.TextList.texts', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1316,
  serialized_end=1371,
)

_POLICYTOPICEVIDENCE_WEBSITELIST = _descriptor.Descriptor(
  name='WebsiteList',
  full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.WebsiteList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='websites', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.WebsiteList.websites', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1373,
  serialized_end=1434,
)

_POLICYTOPICEVIDENCE_DESTINATIONTEXTLIST = _descriptor.Descriptor(
  name='DestinationTextList',
  full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationTextList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination_texts', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationTextList.destination_texts', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1436,
  serialized_end=1514,
)

_POLICYTOPICEVIDENCE_DESTINATIONMISMATCH = _descriptor.Descriptor(
  name='DestinationMismatch',
  full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationMismatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url_types', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationMismatch.url_types', index=0,
      number=1, type=14, cpp_type=8, label=3,
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
  serialized_start=1517,
  serialized_end=1686,
)

_POLICYTOPICEVIDENCE = _descriptor.Descriptor(
  name='PolicyTopicEvidence',
  full_name='google.ads.googleads.v0.common.PolicyTopicEvidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_code', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.http_code', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='website_list', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.website_list', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text_list', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.text_list', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.language_code', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_text_list', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.destination_text_list', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='destination_mismatch', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.destination_mismatch', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POLICYTOPICEVIDENCE_TEXTLIST, _POLICYTOPICEVIDENCE_WEBSITELIST, _POLICYTOPICEVIDENCE_DESTINATIONTEXTLIST, _POLICYTOPICEVIDENCE_DESTINATIONMISMATCH, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='google.ads.googleads.v0.common.PolicyTopicEvidence.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=805,
  serialized_end=1695,
)


_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST = _descriptor.Descriptor(
  name='CountryConstraintList',
  full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_targeted_countries', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintList.total_targeted_countries', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintList.countries', index=1,
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
  serialized_start=2198,
  serialized_end=2376,
)

_POLICYTOPICCONSTRAINT_RESELLERCONSTRAINT = _descriptor.Descriptor(
  name='ResellerConstraint',
  full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.ResellerConstraint',
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
  serialized_start=2378,
  serialized_end=2398,
)

_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINT = _descriptor.Descriptor(
  name='CountryConstraint',
  full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_criterion', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraint.country_criterion', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=2400,
  serialized_end=2476,
)

_POLICYTOPICCONSTRAINT = _descriptor.Descriptor(
  name='PolicyTopicConstraint',
  full_name='google.ads.googleads.v0.common.PolicyTopicConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_constraint_list', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.country_constraint_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reseller_constraint', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.reseller_constraint', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate_missing_in_country_list', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.certificate_missing_in_country_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate_domain_mismatch_in_country_list', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.certificate_domain_mismatch_in_country_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST, _POLICYTOPICCONSTRAINT_RESELLERCONSTRAINT, _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='google.ads.googleads.v0.common.PolicyTopicConstraint.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1698,
  serialized_end=2485,
)

_POLICYVIOLATIONKEY.fields_by_name['policy_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYVIOLATIONKEY.fields_by_name['violating_text'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYVALIDATIONPARAMETER.fields_by_name['ignorable_policy_topics'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICENTRY.fields_by_name['topic'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICENTRY.fields_by_name['type'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_policy__topic__entry__type__pb2._POLICYTOPICENTRYTYPEENUM_POLICYTOPICENTRYTYPE
_POLICYTOPICENTRY.fields_by_name['evidences'].message_type = _POLICYTOPICEVIDENCE
_POLICYTOPICENTRY.fields_by_name['constraints'].message_type = _POLICYTOPICCONSTRAINT
_POLICYTOPICEVIDENCE_TEXTLIST.fields_by_name['texts'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICEVIDENCE_TEXTLIST.containing_type = _POLICYTOPICEVIDENCE
_POLICYTOPICEVIDENCE_WEBSITELIST.fields_by_name['websites'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICEVIDENCE_WEBSITELIST.containing_type = _POLICYTOPICEVIDENCE
_POLICYTOPICEVIDENCE_DESTINATIONTEXTLIST.fields_by_name['destination_texts'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICEVIDENCE_DESTINATIONTEXTLIST.containing_type = _POLICYTOPICEVIDENCE
_POLICYTOPICEVIDENCE_DESTINATIONMISMATCH.fields_by_name['url_types'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_policy__topic__evidence__destination__mismatch__url__type__pb2._POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPEENUM_POLICYTOPICEVIDENCEDESTINATIONMISMATCHURLTYPE
_POLICYTOPICEVIDENCE_DESTINATIONMISMATCH.containing_type = _POLICYTOPICEVIDENCE
_POLICYTOPICEVIDENCE.fields_by_name['http_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_POLICYTOPICEVIDENCE.fields_by_name['website_list'].message_type = _POLICYTOPICEVIDENCE_WEBSITELIST
_POLICYTOPICEVIDENCE.fields_by_name['text_list'].message_type = _POLICYTOPICEVIDENCE_TEXTLIST
_POLICYTOPICEVIDENCE.fields_by_name['language_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICEVIDENCE.fields_by_name['destination_text_list'].message_type = _POLICYTOPICEVIDENCE_DESTINATIONTEXTLIST
_POLICYTOPICEVIDENCE.fields_by_name['destination_mismatch'].message_type = _POLICYTOPICEVIDENCE_DESTINATIONMISMATCH
_POLICYTOPICEVIDENCE.oneofs_by_name['value'].fields.append(
  _POLICYTOPICEVIDENCE.fields_by_name['http_code'])
_POLICYTOPICEVIDENCE.fields_by_name['http_code'].containing_oneof = _POLICYTOPICEVIDENCE.oneofs_by_name['value']
_POLICYTOPICEVIDENCE.oneofs_by_name['value'].fields.append(
  _POLICYTOPICEVIDENCE.fields_by_name['website_list'])
_POLICYTOPICEVIDENCE.fields_by_name['website_list'].containing_oneof = _POLICYTOPICEVIDENCE.oneofs_by_name['value']
_POLICYTOPICEVIDENCE.oneofs_by_name['value'].fields.append(
  _POLICYTOPICEVIDENCE.fields_by_name['text_list'])
_POLICYTOPICEVIDENCE.fields_by_name['text_list'].containing_oneof = _POLICYTOPICEVIDENCE.oneofs_by_name['value']
_POLICYTOPICEVIDENCE.oneofs_by_name['value'].fields.append(
  _POLICYTOPICEVIDENCE.fields_by_name['language_code'])
_POLICYTOPICEVIDENCE.fields_by_name['language_code'].containing_oneof = _POLICYTOPICEVIDENCE.oneofs_by_name['value']
_POLICYTOPICEVIDENCE.oneofs_by_name['value'].fields.append(
  _POLICYTOPICEVIDENCE.fields_by_name['destination_text_list'])
_POLICYTOPICEVIDENCE.fields_by_name['destination_text_list'].containing_oneof = _POLICYTOPICEVIDENCE.oneofs_by_name['value']
_POLICYTOPICEVIDENCE.oneofs_by_name['value'].fields.append(
  _POLICYTOPICEVIDENCE.fields_by_name['destination_mismatch'])
_POLICYTOPICEVIDENCE.fields_by_name['destination_mismatch'].containing_oneof = _POLICYTOPICEVIDENCE.oneofs_by_name['value']
_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST.fields_by_name['total_targeted_countries'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST.fields_by_name['countries'].message_type = _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINT
_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST.containing_type = _POLICYTOPICCONSTRAINT
_POLICYTOPICCONSTRAINT_RESELLERCONSTRAINT.containing_type = _POLICYTOPICCONSTRAINT
_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINT.fields_by_name['country_criterion'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINT.containing_type = _POLICYTOPICCONSTRAINT
_POLICYTOPICCONSTRAINT.fields_by_name['country_constraint_list'].message_type = _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST
_POLICYTOPICCONSTRAINT.fields_by_name['reseller_constraint'].message_type = _POLICYTOPICCONSTRAINT_RESELLERCONSTRAINT
_POLICYTOPICCONSTRAINT.fields_by_name['certificate_missing_in_country_list'].message_type = _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST
_POLICYTOPICCONSTRAINT.fields_by_name['certificate_domain_mismatch_in_country_list'].message_type = _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST
_POLICYTOPICCONSTRAINT.oneofs_by_name['value'].fields.append(
  _POLICYTOPICCONSTRAINT.fields_by_name['country_constraint_list'])
_POLICYTOPICCONSTRAINT.fields_by_name['country_constraint_list'].containing_oneof = _POLICYTOPICCONSTRAINT.oneofs_by_name['value']
_POLICYTOPICCONSTRAINT.oneofs_by_name['value'].fields.append(
  _POLICYTOPICCONSTRAINT.fields_by_name['reseller_constraint'])
_POLICYTOPICCONSTRAINT.fields_by_name['reseller_constraint'].containing_oneof = _POLICYTOPICCONSTRAINT.oneofs_by_name['value']
_POLICYTOPICCONSTRAINT.oneofs_by_name['value'].fields.append(
  _POLICYTOPICCONSTRAINT.fields_by_name['certificate_missing_in_country_list'])
_POLICYTOPICCONSTRAINT.fields_by_name['certificate_missing_in_country_list'].containing_oneof = _POLICYTOPICCONSTRAINT.oneofs_by_name['value']
_POLICYTOPICCONSTRAINT.oneofs_by_name['value'].fields.append(
  _POLICYTOPICCONSTRAINT.fields_by_name['certificate_domain_mismatch_in_country_list'])
_POLICYTOPICCONSTRAINT.fields_by_name['certificate_domain_mismatch_in_country_list'].containing_oneof = _POLICYTOPICCONSTRAINT.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['PolicyViolationKey'] = _POLICYVIOLATIONKEY
DESCRIPTOR.message_types_by_name['PolicyValidationParameter'] = _POLICYVALIDATIONPARAMETER
DESCRIPTOR.message_types_by_name['PolicyTopicEntry'] = _POLICYTOPICENTRY
DESCRIPTOR.message_types_by_name['PolicyTopicEvidence'] = _POLICYTOPICEVIDENCE
DESCRIPTOR.message_types_by_name['PolicyTopicConstraint'] = _POLICYTOPICCONSTRAINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyViolationKey = _reflection.GeneratedProtocolMessageType('PolicyViolationKey', (_message.Message,), dict(
  DESCRIPTOR = _POLICYVIOLATIONKEY,
  __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
  ,
  __doc__ = """Key of the violation. The key is used for referring to a violation when
  filing an exemption request.
  
  
  Attributes:
      policy_name:
          Unique ID of the violated policy.
      violating_text:
          The text that violates the policy if specified. Otherwise,
          refers to the policy in general (e.g., when requesting to be
          exempt from the whole policy). If not specified for criterion
          exemptions, the whole policy is implied. Must be specified for
          ad exemptions.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyViolationKey)
  ))
_sym_db.RegisterMessage(PolicyViolationKey)

PolicyValidationParameter = _reflection.GeneratedProtocolMessageType('PolicyValidationParameter', (_message.Message,), dict(
  DESCRIPTOR = _POLICYVALIDATIONPARAMETER,
  __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
  ,
  __doc__ = """Parameter for controlling how policy checking is done.
  
  
  Attributes:
      ignorable_policy_topics:
          The list of policy topics that should not cause a
          PolicyFindingError to be reported. This field is currently
          only compatible with Enhanced Text Ad. It corresponds to the
          PolicyTopicEntry.topic field.  Resources violating these
          policies will be saved, but will not be eligible to serve.
          They may begin serving at a later time due to a change in
          policies, re-review of the resource, or a change in advertiser
          certificates.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyValidationParameter)
  ))
_sym_db.RegisterMessage(PolicyValidationParameter)

PolicyTopicEntry = _reflection.GeneratedProtocolMessageType('PolicyTopicEntry', (_message.Message,), dict(
  DESCRIPTOR = _POLICYTOPICENTRY,
  __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
  ,
  __doc__ = """Policy finding attached to a resource (e.g. alcohol policy associated
  with a site that sells alcohol).
  
  Each PolicyTopicEntry has a topic that indicates the specific ads policy
  the entry is about and a type to indicate the effect that the entry will
  have on serving. It may optionally have one or more evidences that
  indicate the reason for the finding. It may also optionally have one or
  more constraints that provide details about how serving may be
  restricted.
  
  Next tag: 5
  
  
  Attributes:
      topic:
          Policy topic this finding refers to. For example, "ALCOHOL",
          "TRADEMARKS\_IN\_AD\_TEXT", or "DESTINATION\_NOT\_WORKING".
          The set of possible policy topics is not fixed for a
          particular API version and may change at any time.
      type:
          Describes the negative or positive effect this policy will
          have on serving.
      evidences:
          Additional information that explains policy finding (e.g. the
          brand name for a trademark finding).
      constraints:
          Indicates how serving of this resource may be affected (e.g.
          not serving in a country).
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicEntry)
  ))
_sym_db.RegisterMessage(PolicyTopicEntry)

PolicyTopicEvidence = _reflection.GeneratedProtocolMessageType('PolicyTopicEvidence', (_message.Message,), dict(

  TextList = _reflection.GeneratedProtocolMessageType('TextList', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICEVIDENCE_TEXTLIST,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """A list of fragments of text that violated a policy.
    
    Next Id: 2
    
    
    Attributes:
        texts:
            The fragments of text from the resource that caused the policy
            finding.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicEvidence.TextList)
    ))
  ,

  WebsiteList = _reflection.GeneratedProtocolMessageType('WebsiteList', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICEVIDENCE_WEBSITELIST,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """A list of websites that caused a policy finding. Used for
    ONE\_WEBSITE\_PER\_AD\_GROUP policy topic, for example. In case there
    are more than five websites, only the top five (those that appear in
    resources the most) will be listed here.
    
    Next Id: 2
    
    
    Attributes:
        websites:
            Websites that caused the policy finding.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicEvidence.WebsiteList)
    ))
  ,

  DestinationTextList = _reflection.GeneratedProtocolMessageType('DestinationTextList', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICEVIDENCE_DESTINATIONTEXTLIST,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """A list of strings found in a destination page that caused a policy
    finding.
    
    Next Id: 2
    
    
    Attributes:
        destination_texts:
            List of text found in the resource's destination page.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationTextList)
    ))
  ,

  DestinationMismatch = _reflection.GeneratedProtocolMessageType('DestinationMismatch', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICEVIDENCE_DESTINATIONMISMATCH,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """Evidence of mismatches between the URLs of a resource.
    
    Next Id: 2
    
    
    Attributes:
        url_types:
            The set of URLs that did not match each other.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicEvidence.DestinationMismatch)
    ))
  ,
  DESCRIPTOR = _POLICYTOPICEVIDENCE,
  __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
  ,
  __doc__ = """Additional information that explains a policy finding.
  
  Next Id: 8
  
  
  Attributes:
      value:
          Specific evidence information depending on the evidence type.
      http_code:
          HTTP code returned when the final URL was crawled.
      website_list:
          List of websites linked with this resource.
      text_list:
          List of evidence found in the text of a resource.
      language_code:
          The language the resource was detected to be written in. This
          is an IETF language tag such as "en-US".
      destination_text_list:
          The text in the destination of the resource that is causing a
          policy finding.
      destination_mismatch:
          Mismatch between the destinations of a resource's URLs.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicEvidence)
  ))
_sym_db.RegisterMessage(PolicyTopicEvidence)
_sym_db.RegisterMessage(PolicyTopicEvidence.TextList)
_sym_db.RegisterMessage(PolicyTopicEvidence.WebsiteList)
_sym_db.RegisterMessage(PolicyTopicEvidence.DestinationTextList)
_sym_db.RegisterMessage(PolicyTopicEvidence.DestinationMismatch)

PolicyTopicConstraint = _reflection.GeneratedProtocolMessageType('PolicyTopicConstraint', (_message.Message,), dict(

  CountryConstraintList = _reflection.GeneratedProtocolMessageType('CountryConstraintList', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINTLIST,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """A list of countries where a resource's serving is constrained.
    
    Next Id: 3
    
    
    Attributes:
        total_targeted_countries:
            Total number of countries targeted by the resource.
        countries:
            Countries in which serving is restricted.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraintList)
    ))
  ,

  ResellerConstraint = _reflection.GeneratedProtocolMessageType('ResellerConstraint', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICCONSTRAINT_RESELLERCONSTRAINT,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """Indicates that a policy topic was constrained due to disapproval of the
    website for reseller purposes.
    
    Next Id: 1
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicConstraint.ResellerConstraint)
    ))
  ,

  CountryConstraint = _reflection.GeneratedProtocolMessageType('CountryConstraint', (_message.Message,), dict(
    DESCRIPTOR = _POLICYTOPICCONSTRAINT_COUNTRYCONSTRAINT,
    __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
    ,
    __doc__ = """Indicates that a resource's ability to serve in a particular country is
    constrained.
    
    Next Id: 2
    
    
    Attributes:
        country_criterion:
            Geo target constant resource name of the country in which
            serving is constrained.
    """,
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicConstraint.CountryConstraint)
    ))
  ,
  DESCRIPTOR = _POLICYTOPICCONSTRAINT,
  __module__ = 'google.ads.google_ads.v0.proto.common.policy_pb2'
  ,
  __doc__ = """Describes the effect on serving that a policy topic entry will have.
  
  Next Id: 5
  
  
  Attributes:
      value:
          Specific information about the constraint.
      country_constraint_list:
          Countries where the resource cannot serve.
      reseller_constraint:
          Reseller constraint.
      certificate_missing_in_country_list:
          Countries where a certificate is required for serving.
      certificate_domain_mismatch_in_country_list:
          Countries where the resource's domain is not covered by the
          certificates associated with it.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.PolicyTopicConstraint)
  ))
_sym_db.RegisterMessage(PolicyTopicConstraint)
_sym_db.RegisterMessage(PolicyTopicConstraint.CountryConstraintList)
_sym_db.RegisterMessage(PolicyTopicConstraint.ResellerConstraint)
_sym_db.RegisterMessage(PolicyTopicConstraint.CountryConstraint)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.commonB\013PolicyProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common'))
# @@protoc_insertion_point(module_scope)
