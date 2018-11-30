# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/criterion_error.proto

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
  name='google/ads/googleads_v0/proto/errors/criterion_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\n:google/ads/googleads_v0/proto/errors/criterion_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xa0\x18\n\x12\x43riterionErrorEnum\"\x89\x18\n\x0e\x43riterionError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x1a\n\x16\x43ONCRETE_TYPE_REQUIRED\x10\x02\x12\x1d\n\x19INVALID_EXCLUDED_CATEGORY\x10\x03\x12\x18\n\x14INVALID_KEYWORD_TEXT\x10\x04\x12\x19\n\x15KEYWORD_TEXT_TOO_LONG\x10\x05\x12\x1e\n\x1aKEYWORD_HAS_TOO_MANY_WORDS\x10\x06\x12\x1d\n\x19KEYWORD_HAS_INVALID_CHARS\x10\x07\x12\x19\n\x15INVALID_PLACEMENT_URL\x10\x08\x12\x15\n\x11INVALID_USER_LIST\x10\t\x12\x19\n\x15INVALID_USER_INTEREST\x10\n\x12$\n INVALID_FORMAT_FOR_PLACEMENT_URL\x10\x0b\x12\x1d\n\x19PLACEMENT_URL_IS_TOO_LONG\x10\x0c\x12\"\n\x1ePLACEMENT_URL_HAS_ILLEGAL_CHAR\x10\r\x12,\n(PLACEMENT_URL_HAS_MULTIPLE_SITES_IN_LINE\x10\x0e\x12\x39\n5PLACEMENT_IS_NOT_AVAILABLE_FOR_TARGETING_OR_EXCLUSION\x10\x0f\x12\x16\n\x12INVALID_TOPIC_PATH\x10\x10\x12\x1e\n\x1aINVALID_YOUTUBE_CHANNEL_ID\x10\x11\x12\x1c\n\x18INVALID_YOUTUBE_VIDEO_ID\x10\x12\x12\'\n#YOUTUBE_VERTICAL_CHANNEL_DEPRECATED\x10\x13\x12*\n&YOUTUBE_DEMOGRAPHIC_CHANNEL_DEPRECATED\x10\x14\x12\x1b\n\x17YOUTUBE_URL_UNSUPPORTED\x10\x15\x12 \n\x1c\x43\x41NNOT_EXCLUDE_CRITERIA_TYPE\x10\x16\x12\x1c\n\x18\x43\x41NNOT_ADD_CRITERIA_TYPE\x10\x17\x12\x1a\n\x16INVALID_PRODUCT_FILTER\x10\x18\x12\x1b\n\x17PRODUCT_FILTER_TOO_LONG\x10\x19\x12$\n CANNOT_EXCLUDE_SIMILAR_USER_LIST\x10\x1a\x12\x1f\n\x1b\x43\x41NNOT_ADD_CLOSED_USER_LIST\x10\x1b\x12:\n6CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_ONLY_CAMPAIGNS\x10\x1c\x12\x35\n1CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_CAMPAIGNS\x10\x1d\x12\x37\n3CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SHOPPING_CAMPAIGNS\x10\x1e\x12\x31\n-CANNOT_ADD_USER_INTERESTS_TO_SEARCH_CAMPAIGNS\x10\x1f\x12\x39\n5CANNOT_SET_BIDS_ON_CRITERION_TYPE_IN_SEARCH_CAMPAIGNS\x10 \x12\x37\n3CANNOT_ADD_URLS_TO_CRITERION_TYPE_FOR_CAMPAIGN_TYPE\x10!\x12\x16\n\x12INVALID_IP_ADDRESS\x10\"\x12\x15\n\x11INVALID_IP_FORMAT\x10#\x12\x16\n\x12INVALID_MOBILE_APP\x10$\x12\x1f\n\x1bINVALID_MOBILE_APP_CATEGORY\x10%\x12\x18\n\x14INVALID_CRITERION_ID\x10&\x12\x1b\n\x17\x43\x41NNOT_TARGET_CRITERION\x10\'\x12$\n CANNOT_TARGET_OBSOLETE_CRITERION\x10(\x12\"\n\x1e\x43RITERION_ID_AND_TYPE_MISMATCH\x10)\x12\x1c\n\x18INVALID_PROXIMITY_RADIUS\x10*\x12\"\n\x1eINVALID_PROXIMITY_RADIUS_UNITS\x10+\x12 \n\x1cINVALID_STREETADDRESS_LENGTH\x10,\x12\x1b\n\x17INVALID_CITYNAME_LENGTH\x10-\x12\x1d\n\x19INVALID_REGIONCODE_LENGTH\x10.\x12\x1d\n\x19INVALID_REGIONNAME_LENGTH\x10/\x12\x1d\n\x19INVALID_POSTALCODE_LENGTH\x10\x30\x12\x18\n\x14INVALID_COUNTRY_CODE\x10\x31\x12\x14\n\x10INVALID_LATITUDE\x10\x32\x12\x15\n\x11INVALID_LONGITUDE\x10\x33\x12\x36\n2PROXIMITY_GEOPOINT_AND_ADDRESS_BOTH_CANNOT_BE_NULL\x10\x34\x12\x1d\n\x19INVALID_PROXIMITY_ADDRESS\x10\x35\x12\x1c\n\x18INVALID_USER_DOMAIN_NAME\x10\x36\x12 \n\x1c\x43RITERION_PARAMETER_TOO_LONG\x10\x37\x12&\n\"AD_SCHEDULE_TIME_INTERVALS_OVERLAP\x10\x38\x12\x32\n.AD_SCHEDULE_INTERVAL_CANNOT_SPAN_MULTIPLE_DAYS\x10\x39\x12%\n!AD_SCHEDULE_INVALID_TIME_INTERVAL\x10:\x12\x30\n,AD_SCHEDULE_EXCEEDED_INTERVALS_PER_DAY_LIMIT\x10;\x12/\n+AD_SCHEDULE_CRITERION_ID_MISMATCHING_FIELDS\x10<\x12$\n CANNOT_BID_MODIFY_CRITERION_TYPE\x10=\x12\x32\n.CANNOT_BID_MODIFY_CRITERION_CAMPAIGN_OPTED_OUT\x10>\x12(\n$CANNOT_BID_MODIFY_NEGATIVE_CRITERION\x10?\x12\x1f\n\x1b\x42ID_MODIFIER_ALREADY_EXISTS\x10@\x12\x17\n\x13\x46\x45\x45\x44_ID_NOT_ALLOWED\x10\x41\x12(\n$ACCOUNT_INELIGIBLE_FOR_CRITERIA_TYPE\x10\x42\x12.\n*CRITERIA_TYPE_INVALID_FOR_BIDDING_STRATEGY\x10\x43\x12\x1c\n\x18\x43\x41NNOT_EXCLUDE_CRITERION\x10\x44\x12\x1b\n\x17\x43\x41NNOT_REMOVE_CRITERION\x10\x45\x12\x1a\n\x16PRODUCT_SCOPE_TOO_LONG\x10\x46\x12%\n!PRODUCT_SCOPE_TOO_MANY_DIMENSIONS\x10G\x12\x1e\n\x1aPRODUCT_PARTITION_TOO_LONG\x10H\x12)\n%PRODUCT_PARTITION_TOO_MANY_DIMENSIONS\x10I\x12\x1d\n\x19INVALID_PRODUCT_DIMENSION\x10J\x12\"\n\x1eINVALID_PRODUCT_DIMENSION_TYPE\x10K\x12$\n INVALID_PRODUCT_BIDDING_CATEGORY\x10L\x12\x1c\n\x18MISSING_SHOPPING_SETTING\x10M\x12\x1d\n\x19INVALID_MATCHING_FUNCTION\x10N\x12\x1f\n\x1bLOCATION_FILTER_NOT_ALLOWED\x10O\x12\x1b\n\x17LOCATION_FILTER_INVALID\x10P\x12\x32\n.CANNOT_ATTACH_CRITERIA_AT_CAMPAIGN_AND_ADGROUP\x10Q\x12\x39\n5HOTEL_LENGTH_OF_STAY_OVERLAPS_WITH_EXISTING_CRITERION\x10R\x12\x41\n=HOTEL_ADVANCE_BOOKING_WINDOW_OVERLAPS_WITH_EXISTING_CRITERION\x10S\x12.\n*FIELD_INCOMPATIBLE_WITH_NEGATIVE_TARGETING\x10TB\xc9\x01\n\"com.google.ads.googleads.v0.errorsB\x13\x43riterionErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_CRITERIONERRORENUM_CRITERIONERROR = _descriptor.EnumDescriptor(
  name='CriterionError',
  full_name='google.ads.googleads.v0.errors.CriterionErrorEnum.CriterionError',
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
      name='CONCRETE_TYPE_REQUIRED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_EXCLUDED_CATEGORY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_KEYWORD_TEXT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_TEXT_TOO_LONG', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_HAS_TOO_MANY_WORDS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEYWORD_HAS_INVALID_CHARS', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PLACEMENT_URL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_LIST', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_INTEREST', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FORMAT_FOR_PLACEMENT_URL', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEMENT_URL_IS_TOO_LONG', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEMENT_URL_HAS_ILLEGAL_CHAR', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEMENT_URL_HAS_MULTIPLE_SITES_IN_LINE', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLACEMENT_IS_NOT_AVAILABLE_FOR_TARGETING_OR_EXCLUSION', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_TOPIC_PATH', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_YOUTUBE_CHANNEL_ID', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_YOUTUBE_VIDEO_ID', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_VERTICAL_CHANNEL_DEPRECATED', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_DEMOGRAPHIC_CHANNEL_DEPRECATED', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE_URL_UNSUPPORTED', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_EXCLUDE_CRITERIA_TYPE', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_CRITERIA_TYPE', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRODUCT_FILTER', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_FILTER_TOO_LONG', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_EXCLUDE_SIMILAR_USER_LIST', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_CLOSED_USER_LIST', index=27, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_ONLY_CAMPAIGNS', index=28, number=28,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SEARCH_CAMPAIGNS', index=29, number=29,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_DISPLAY_ONLY_LISTS_TO_SHOPPING_CAMPAIGNS', index=30, number=30,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_USER_INTERESTS_TO_SEARCH_CAMPAIGNS', index=31, number=31,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_SET_BIDS_ON_CRITERION_TYPE_IN_SEARCH_CAMPAIGNS', index=32, number=32,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ADD_URLS_TO_CRITERION_TYPE_FOR_CAMPAIGN_TYPE', index=33, number=33,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_IP_ADDRESS', index=34, number=34,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_IP_FORMAT', index=35, number=35,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MOBILE_APP', index=36, number=36,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MOBILE_APP_CATEGORY', index=37, number=37,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CRITERION_ID', index=38, number=38,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_CRITERION', index=39, number=39,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_TARGET_OBSOLETE_CRITERION', index=40, number=40,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITERION_ID_AND_TYPE_MISMATCH', index=41, number=41,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PROXIMITY_RADIUS', index=42, number=42,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PROXIMITY_RADIUS_UNITS', index=43, number=43,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_STREETADDRESS_LENGTH', index=44, number=44,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CITYNAME_LENGTH', index=45, number=45,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REGIONCODE_LENGTH', index=46, number=46,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_REGIONNAME_LENGTH', index=47, number=47,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_POSTALCODE_LENGTH', index=48, number=48,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_COUNTRY_CODE', index=49, number=49,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LATITUDE', index=50, number=50,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_LONGITUDE', index=51, number=51,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXIMITY_GEOPOINT_AND_ADDRESS_BOTH_CANNOT_BE_NULL', index=52, number=52,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PROXIMITY_ADDRESS', index=53, number=53,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_USER_DOMAIN_NAME', index=54, number=54,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITERION_PARAMETER_TOO_LONG', index=55, number=55,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_SCHEDULE_TIME_INTERVALS_OVERLAP', index=56, number=56,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_SCHEDULE_INTERVAL_CANNOT_SPAN_MULTIPLE_DAYS', index=57, number=57,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_SCHEDULE_INVALID_TIME_INTERVAL', index=58, number=58,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_SCHEDULE_EXCEEDED_INTERVALS_PER_DAY_LIMIT', index=59, number=59,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AD_SCHEDULE_CRITERION_ID_MISMATCHING_FIELDS', index=60, number=60,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_BID_MODIFY_CRITERION_TYPE', index=61, number=61,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_BID_MODIFY_CRITERION_CAMPAIGN_OPTED_OUT', index=62, number=62,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_BID_MODIFY_NEGATIVE_CRITERION', index=63, number=63,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BID_MODIFIER_ALREADY_EXISTS', index=64, number=64,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEED_ID_NOT_ALLOWED', index=65, number=65,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_INELIGIBLE_FOR_CRITERIA_TYPE', index=66, number=66,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITERIA_TYPE_INVALID_FOR_BIDDING_STRATEGY', index=67, number=67,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_EXCLUDE_CRITERION', index=68, number=68,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_REMOVE_CRITERION', index=69, number=69,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_SCOPE_TOO_LONG', index=70, number=70,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_SCOPE_TOO_MANY_DIMENSIONS', index=71, number=71,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_PARTITION_TOO_LONG', index=72, number=72,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_PARTITION_TOO_MANY_DIMENSIONS', index=73, number=73,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRODUCT_DIMENSION', index=74, number=74,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRODUCT_DIMENSION_TYPE', index=75, number=75,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PRODUCT_BIDDING_CATEGORY', index=76, number=76,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MISSING_SHOPPING_SETTING', index=77, number=77,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_MATCHING_FUNCTION', index=78, number=78,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FILTER_NOT_ALLOWED', index=79, number=79,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_FILTER_INVALID', index=80, number=80,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_ATTACH_CRITERIA_AT_CAMPAIGN_AND_ADGROUP', index=81, number=81,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_LENGTH_OF_STAY_OVERLAPS_WITH_EXISTING_CRITERION', index=82, number=82,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOTEL_ADVANCE_BOOKING_WINDOW_OVERLAPS_WITH_EXISTING_CRITERION', index=83, number=83,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIELD_INCOMPATIBLE_WITH_NEGATIVE_TARGETING', index=84, number=84,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=118,
  serialized_end=3199,
)
_sym_db.RegisterEnumDescriptor(_CRITERIONERRORENUM_CRITERIONERROR)


_CRITERIONERRORENUM = _descriptor.Descriptor(
  name='CriterionErrorEnum',
  full_name='google.ads.googleads.v0.errors.CriterionErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CRITERIONERRORENUM_CRITERIONERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=3199,
)

_CRITERIONERRORENUM_CRITERIONERROR.containing_type = _CRITERIONERRORENUM
DESCRIPTOR.message_types_by_name['CriterionErrorEnum'] = _CRITERIONERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CriterionErrorEnum = _reflection.GeneratedProtocolMessageType('CriterionErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _CRITERIONERRORENUM,
  __module__ = 'google.ads.google_ads.v0.proto.errors.criterion_error_pb2'
  ,
  __doc__ = """Container for enum describing possible criterion errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.CriterionErrorEnum)
  ))
_sym_db.RegisterMessage(CriterionErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB\023CriterionErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
