# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/common/feed_common.proto

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
  name='google/ads/googleads_v0/proto/common/feed_common.proto',
  package='google.ads.googleads.v0.common',
  syntax='proto3',
  serialized_pb=_b('\n6google/ads/googleads_v0/proto/common/feed_common.proto\x12\x1egoogle.ads.googleads.v0.common\x1a\x1egoogle/protobuf/wrappers.proto\"p\n\x05Price\x12\x33\n\rcurrency_code\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\ramount_micros\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\xc5\x01\n\"com.google.ads.googleads.v0.commonB\x0f\x46\x65\x65\x64\x43ommonProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_PRICE = _descriptor.Descriptor(
  name='Price',
  full_name='google.ads.googleads.v0.common.Price',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency_code', full_name='google.ads.googleads.v0.common.Price.currency_code', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount_micros', full_name='google.ads.googleads.v0.common.Price.amount_micros', index=1,
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
  serialized_start=122,
  serialized_end=234,
)

_PRICE.fields_by_name['currency_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PRICE.fields_by_name['amount_micros'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['Price'] = _PRICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Price = _reflection.GeneratedProtocolMessageType('Price', (_message.Message,), dict(
  DESCRIPTOR = _PRICE,
  __module__ = 'google.ads.google_ads.v0.proto.common.feed_common_pb2'
  ,
  __doc__ = """Represents a price in a particular currency.
  
  
  Attributes:
      currency_code:
          Three-character ISO 4217 currency code.
      amount_micros:
          Amount in micros. One million is equivalent to one unit.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.common.Price)
  ))
_sym_db.RegisterMessage(Price)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.commonB\017FeedCommonProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Common\312\002\036Google\\Ads\\GoogleAds\\V0\\Common'))
# @@protoc_insertion_point(module_scope)
