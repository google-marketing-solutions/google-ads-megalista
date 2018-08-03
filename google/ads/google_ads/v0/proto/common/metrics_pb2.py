# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/metrics.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/common/metrics.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_pb=_b('\n2google/ads/googleads_v0/proto/common/metrics.proto\x12\x1egoogle.ads.googleads.v0.common\x1a\x1egoogle/protobuf/wrappers.proto\"\xf7\x13\n\x07Metrics\x12\x39\n\x13\x61ll_conversion_rate\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12:\n\x14\x61ll_conversion_value\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0f\x61ll_conversions\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x44\n\x1e\x61ll_conversions_value_per_cost\x18> \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12K\n%all_conversions_value_per_interaction\x18= \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x32\n\x0c\x61verage_cost\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\x0b\x61verage_cpc\x18\t \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\x0b\x61verage_cpm\x18\n \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x10\x61verage_position\x18\r \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\x0b\x62ounce_rate\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12+\n\x06\x63licks\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12J\n$content_budget_lost_impression_share\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x18\x63ontent_impression_share\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12H\n\"content_rank_lost_impression_share\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0f\x63onversion_rate\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x36\n\x10\x63onversion_value\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12?\n\x19\x63onversion_value_per_cost\x18@ \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x46\n conversion_value_per_interaction\x18? \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\x0b\x63onversions\x18\x19 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\x0b\x63ost_micros\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12=\n\x17\x63ost_per_all_conversion\x18\x1b \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x39\n\x13\x63ost_per_conversion\x18\x1c \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12>\n\x18\x63ross_device_conversions\x18\x1d \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12)\n\x03\x63tr\x18\x1e \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0f\x65ngagement_rate\x18\x1f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\x0b\x65ngagements\x18  \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x30\n\x0bimpressions\x18% \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x10interaction_rate\x18& \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\x0cinteractions\x18\' \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x12invalid_click_rate\x18( \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x33\n\x0einvalid_clicks\x18) \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x14percent_new_visitors\x18* \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\x0bphone_calls\x18+ \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11phone_impressions\x18, \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x38\n\x12phone_through_rate\x18- \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x32\n\x0crelative_ctr\x18. \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12I\n#search_budget_lost_impression_share\x18/ \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12I\n#search_exact_match_impression_share\x18\x31 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12=\n\x17search_impression_share\x18\x32 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12G\n!search_rank_lost_impression_share\x18\x33 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12?\n\x19value_per_all_conversions\x18\x34 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12:\n\x14value_per_conversion\x18\x35 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12=\n\x18view_through_conversions\x18< \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\xc2\x01\n\"com.google.ads.googleads.v0.commonB\x0cMetricsProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_METRICS = _descriptor.Descriptor(
  name='Metrics',
  full_name='google.ads.googleads.v0.common.Metrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_conversion_rate', full_name='google.ads.googleads.v0.common.Metrics.all_conversion_rate', index=0,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_conversion_value', full_name='google.ads.googleads.v0.common.Metrics.all_conversion_value', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_conversions', full_name='google.ads.googleads.v0.common.Metrics.all_conversions', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_conversions_value_per_cost', full_name='google.ads.googleads.v0.common.Metrics.all_conversions_value_per_cost', index=3,
      number=62, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_conversions_value_per_interaction', full_name='google.ads.googleads.v0.common.Metrics.all_conversions_value_per_interaction', index=4,
      number=61, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_cost', full_name='google.ads.googleads.v0.common.Metrics.average_cost', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_cpc', full_name='google.ads.googleads.v0.common.Metrics.average_cpc', index=6,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_cpm', full_name='google.ads.googleads.v0.common.Metrics.average_cpm', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_position', full_name='google.ads.googleads.v0.common.Metrics.average_position', index=8,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bounce_rate', full_name='google.ads.googleads.v0.common.Metrics.bounce_rate', index=9,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clicks', full_name='google.ads.googleads.v0.common.Metrics.clicks', index=10,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_budget_lost_impression_share', full_name='google.ads.googleads.v0.common.Metrics.content_budget_lost_impression_share', index=11,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_impression_share', full_name='google.ads.googleads.v0.common.Metrics.content_impression_share', index=12,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_rank_lost_impression_share', full_name='google.ads.googleads.v0.common.Metrics.content_rank_lost_impression_share', index=13,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_rate', full_name='google.ads.googleads.v0.common.Metrics.conversion_rate', index=14,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_value', full_name='google.ads.googleads.v0.common.Metrics.conversion_value', index=15,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_value_per_cost', full_name='google.ads.googleads.v0.common.Metrics.conversion_value_per_cost', index=16,
      number=64, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversion_value_per_interaction', full_name='google.ads.googleads.v0.common.Metrics.conversion_value_per_interaction', index=17,
      number=63, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conversions', full_name='google.ads.googleads.v0.common.Metrics.conversions', index=18,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_micros', full_name='google.ads.googleads.v0.common.Metrics.cost_micros', index=19,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_per_all_conversion', full_name='google.ads.googleads.v0.common.Metrics.cost_per_all_conversion', index=20,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost_per_conversion', full_name='google.ads.googleads.v0.common.Metrics.cost_per_conversion', index=21,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cross_device_conversions', full_name='google.ads.googleads.v0.common.Metrics.cross_device_conversions', index=22,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctr', full_name='google.ads.googleads.v0.common.Metrics.ctr', index=23,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engagement_rate', full_name='google.ads.googleads.v0.common.Metrics.engagement_rate', index=24,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='engagements', full_name='google.ads.googleads.v0.common.Metrics.engagements', index=25,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='impressions', full_name='google.ads.googleads.v0.common.Metrics.impressions', index=26,
      number=37, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interaction_rate', full_name='google.ads.googleads.v0.common.Metrics.interaction_rate', index=27,
      number=38, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactions', full_name='google.ads.googleads.v0.common.Metrics.interactions', index=28,
      number=39, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invalid_click_rate', full_name='google.ads.googleads.v0.common.Metrics.invalid_click_rate', index=29,
      number=40, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invalid_clicks', full_name='google.ads.googleads.v0.common.Metrics.invalid_clicks', index=30,
      number=41, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent_new_visitors', full_name='google.ads.googleads.v0.common.Metrics.percent_new_visitors', index=31,
      number=42, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_calls', full_name='google.ads.googleads.v0.common.Metrics.phone_calls', index=32,
      number=43, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_impressions', full_name='google.ads.googleads.v0.common.Metrics.phone_impressions', index=33,
      number=44, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_through_rate', full_name='google.ads.googleads.v0.common.Metrics.phone_through_rate', index=34,
      number=45, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='relative_ctr', full_name='google.ads.googleads.v0.common.Metrics.relative_ctr', index=35,
      number=46, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_budget_lost_impression_share', full_name='google.ads.googleads.v0.common.Metrics.search_budget_lost_impression_share', index=36,
      number=47, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_exact_match_impression_share', full_name='google.ads.googleads.v0.common.Metrics.search_exact_match_impression_share', index=37,
      number=49, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_impression_share', full_name='google.ads.googleads.v0.common.Metrics.search_impression_share', index=38,
      number=50, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='search_rank_lost_impression_share', full_name='google.ads.googleads.v0.common.Metrics.search_rank_lost_impression_share', index=39,
      number=51, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_per_all_conversions', full_name='google.ads.googleads.v0.common.Metrics.value_per_all_conversions', index=40,
      number=52, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_per_conversion', full_name='google.ads.googleads.v0.common.Metrics.value_per_conversion', index=41,
      number=53, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='view_through_conversions', full_name='google.ads.googleads.v0.common.Metrics.view_through_conversions', index=42,
      number=60, type=11, cpp_type=10, label=1,
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
  serialized_start=119,
  serialized_end=2670,
)

_METRICS.fields_by_name['all_conversion_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['all_conversion_value'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['all_conversions'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['all_conversions_value_per_cost'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['all_conversions_value_per_interaction'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['average_cost'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['average_cpc'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['average_cpm'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['average_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['bounce_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['clicks'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['content_budget_lost_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['content_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['content_rank_lost_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['conversion_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['conversion_value'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['conversion_value_per_cost'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['conversion_value_per_interaction'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['conversions'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['cost_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['cost_per_all_conversion'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['cost_per_conversion'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['cross_device_conversions'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['ctr'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['engagement_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['engagements'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['impressions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['interaction_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['interactions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['invalid_click_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['invalid_clicks'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['percent_new_visitors'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['phone_calls'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['phone_impressions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_METRICS.fields_by_name['phone_through_rate'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['relative_ctr'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['search_budget_lost_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['search_exact_match_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['search_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['search_rank_lost_impression_share'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['value_per_all_conversions'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['value_per_conversion'].message_type = google_dot_protobuf_dot_wrappers__pb2._DOUBLEVALUE
_METRICS.fields_by_name['view_through_conversions'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['Metrics'] = _METRICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), dict(
  DESCRIPTOR = _METRICS,
  __module__ = 'google.ads.googleads_v0.proto.common.metrics_pb2'
  ,
  __doc__ = """Metrics data.
  
  
  Attributes:
      all_conversion_rate:
          All conversions divided by the number of ad interactions.
      all_conversion_value:
          The total value of all conversions.
      all_conversions:
          The total number of conversions. This includes "Conversions"
          plus conversions that have their "Include in Conversions"
          setting unchecked.
      all_conversions_value_per_cost:
          The value of all conversions divided by the total cost of ad
          interactions (such as clicks for text ads or views for video
          ads).
      all_conversions_value_per_interaction:
          The value of all conversions divided by the total number of
          interactions.
      average_cost:
          The average amount you pay per interaction. This amount is the
          total cost of your ads divided by the total number of
          interactions.
      average_cpc:
          The total cost of all clicks divided by the total number of
          clicks received.
      average_cpm:
          Average cost-per-thousand impressions (CPM).
      average_position:
          Your ad's position relative to those of other advertisers.
      bounce_rate:
          Percentage of clicks where the user only visited a single page
          on your site. Imported from Google Analytics.
      clicks:
          The number of clicks.
      content_budget_lost_impression_share:
          The estimated percent of times that your ad was eligible to
          show on the Display Network but didn't because your budget was
          too low. Note: Content budget lost impression share is
          reported in the range of 0 to 0.9. Any value above 0.9 is
          reported as 0.9001.
      content_impression_share:
          The impressions you've received on the Display Network divided
          by the estimated number of impressions you were eligible to
          receive. Note: Content impression share is reported in the
          range of 0.1 to 1. Any value below 0.1 is reported as 0.0999.
      content_rank_lost_impression_share:
          The estimated percentage of impressions on the Display Network
          that your ads didn't receive due to poor Ad Rank. Note:
          Content rank lost impression share is reported in the range of
          0 to 0.9. Any value above 0.9 is reported as 0.9001.
      conversion_rate:
          Conversions divided by the number of ad interactions (such as
          clicks for text ads or views for video ads).
      conversion_value:
          The total value of conversions.
      conversion_value_per_cost:
          The value of conversions divided by the cost of ad
          interactions.
      conversion_value_per_interaction:
          The value of conversions divided by the number of ad
          interactions.
      conversions:
          The number of conversions. This only includes conversion
          actions which have "Include in Conversions" checked.
      cost_micros:
          The sum of your cost-per-click (CPC) and cost-per-thousand
          impressions (CPM) costs during this period.
      cost_per_all_conversion:
          The cost of ad interactions divided by all conversions.
      cost_per_conversion:
          The cost of ad interactions divided by conversions.
      cross_device_conversions:
          Conversions from when a customer clicks on an AdWords ad on
          one device, then converts on a different device or browser.
          Cross-device conversions are already included in
          all\_conversions.
      ctr:
          The number of clicks your ad receives (Clicks) divided by the
          number of times your ad is shown (Impressions).
      engagement_rate:
          How often people engage with your ad after it's shown to them.
          This is the number of ad expansions divided by the number of
          times your ad is shown.
      engagements:
          The number of engagements. An engagement occurs when a viewer
          expands your Lightbox ad. Also, in the future, other ad types
          may support engagement metrics.
      impressions:
          Count of how often your ad has appeared on a search results
          page or website on the Google Network.
      interaction_rate:
          How often people interact with your ad after it is shown to
          them. This is the number of interactions divided by the number
          of times your ad is shown.
      interactions:
          The number of interactions. An interaction is the main user
          action associated with an ad format-clicks for text and
          shopping ads, views for video ads, and so on.
      invalid_click_rate:
          The percentage of clicks filtered out of your total number of
          clicks (filtered + non-filtered clicks) during the reporting
          period.
      invalid_clicks:
          Number of clicks Google considers illegitimate and doesn't
          charge you for.
      percent_new_visitors:
          Percentage of first-time sessions (from people who had never
          visited your site before). Imported from Google Analytics.
      phone_calls:
          Number of offline phone calls.
      phone_impressions:
          Number of offline phone impressions.
      phone_through_rate:
          Number of phone calls received (phone\_calls) divided by the
          number of times your phone number is shown
          (phone\_impressions).
      relative_ctr:
          Your clickthrough rate (Ctr) divided by the average
          clickthrough rate of all advertisers on the websites that show
          your ads. Measures how your ads perform on Display Network
          sites compared to other ads on the same sites.
      search_budget_lost_impression_share:
          The estimated percent of times that your ad was eligible to
          show on the Search Network but didn't because your budget was
          too low. Note: Search budget lost impression share is reported
          in the range of 0 to 0.9. Any value above 0.9 is reported as
          0.9001.
      search_exact_match_impression_share:
          The impressions you've received divided by the estimated
          number of impressions you were eligible to receive on the
          Search Network for search terms that matched your keywords
          exactly (or were close variants of your keyword), regardless
          of your keyword match types. Note: Search exact match
          impression share is reported in the range of 0.1 to 1. Any
          value below 0.1 is reported as 0.0999.
      search_impression_share:
          The impressions you've received on the Search Network divided
          by the estimated number of impressions you were eligible to
          receive. Note: Search impression share is reported in the
          range of 0.1 to 1. Any value below 0.1 is reported as 0.0999.
      search_rank_lost_impression_share:
          The estimated percentage of impressions on the Search Network
          that your ads didn't receive due to poor Ad Rank. Note: Search
          rank lost impression share is reported in the range of 0 to
          0.9. Any value above 0.9 is reported as 0.9001.
      value_per_all_conversions:
          The value of all conversions divided by the number of all
          conversions.
      value_per_conversion:
          The value of conversions divided by the number of conversions.
      view_through_conversions:
          The total number of view-through conversions. These happen
          when a customer sees an image or rich media ad, then later
          completes a conversion on your site without interacting with
          (e.g., clicking on) another ad.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.Metrics)
  ))
_sym_db.RegisterMessage(Metrics)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.commonB\014MetricsProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common'))
# @@protoc_insertion_point(module_scope)
