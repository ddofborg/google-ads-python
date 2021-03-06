# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/ad_group_feed.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v0.proto.common import matching_function_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_matching__function__pb2
from google.ads.google_ads.v0.proto.enums import feed_link_status_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_feed__link__status__pb2
from google.ads.google_ads.v0.proto.enums import placeholder_type_pb2 as google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_placeholder__type__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v0/proto/resources/ad_group_feed.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\n;google/ads/googleads_v0/proto/resources/ad_group_feed.proto\x12!google.ads.googleads.v0.resources\x1a<google/ads/googleads_v0/proto/common/matching_function.proto\x1a:google/ads/googleads_v0/proto/enums/feed_link_status.proto\x1a:google/ads/googleads_v0/proto/enums/placeholder_type.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xfe\x02\n\x0b\x41\x64GroupFeed\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12*\n\x04\x66\x65\x65\x64\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x61\x64_group\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12]\n\x11placeholder_types\x18\x04 \x03(\x0e\x32\x42.google.ads.googleads.v0.enums.PlaceholderTypeEnum.PlaceholderType\x12K\n\x11matching_function\x18\x05 \x01(\x0b\x32\x30.google.ads.googleads.v0.common.MatchingFunction\x12P\n\x06status\x18\x06 \x01(\x0e\x32@.google.ads.googleads.v0.enums.FeedLinkStatusEnum.FeedLinkStatusB\xd5\x01\n%com.google.ads.googleads.v0.resourcesB\x10\x41\x64GroupFeedProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_matching__function__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_feed__link__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_placeholder__type__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_ADGROUPFEED = _descriptor.Descriptor(
  name='AdGroupFeed',
  full_name='google.ads.googleads.v0.resources.AdGroupFeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.AdGroupFeed.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed', full_name='google.ads.googleads.v0.resources.AdGroupFeed.feed', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_group', full_name='google.ads.googleads.v0.resources.AdGroupFeed.ad_group', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='placeholder_types', full_name='google.ads.googleads.v0.resources.AdGroupFeed.placeholder_types', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matching_function', full_name='google.ads.googleads.v0.resources.AdGroupFeed.matching_function', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v0.resources.AdGroupFeed.status', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=313,
  serialized_end=695,
)

_ADGROUPFEED.fields_by_name['feed'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPFEED.fields_by_name['ad_group'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_ADGROUPFEED.fields_by_name['placeholder_types'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_placeholder__type__pb2._PLACEHOLDERTYPEENUM_PLACEHOLDERTYPE
_ADGROUPFEED.fields_by_name['matching_function'].message_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_common_dot_matching__function__pb2._MATCHINGFUNCTION
_ADGROUPFEED.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads__v0_dot_proto_dot_enums_dot_feed__link__status__pb2._FEEDLINKSTATUSENUM_FEEDLINKSTATUS
DESCRIPTOR.message_types_by_name['AdGroupFeed'] = _ADGROUPFEED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupFeed = _reflection.GeneratedProtocolMessageType('AdGroupFeed', (_message.Message,), dict(
  DESCRIPTOR = _ADGROUPFEED,
  __module__ = 'google.ads.google_ads.v0.proto.resources.ad_group_feed_pb2'
  ,
  __doc__ = """An ad group feed.
  
  
  Attributes:
      resource_name:
          The resource name of the ad group feed. Ad group feed resource
          names have the form:  \`customers/{customer\_id}/adGroupFeeds/
          {ad\_group\_id}\_{feed\_id}
      feed:
          The feed being linked to the ad group.
      ad_group:
          The ad group being linked to the feed.
      placeholder_types:
          Indicates which placeholder types the feed may populate under
          the connected ad group. Required.
      matching_function:
          Matching function associated with the AdGroupFeed. The
          matching function is used to filter the set of feed items
          selected. Required.
      status:
          Status of the ad group feed. This field is read-only.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.AdGroupFeed)
  ))
_sym_db.RegisterMessage(AdGroupFeed)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\020AdGroupFeedProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)
