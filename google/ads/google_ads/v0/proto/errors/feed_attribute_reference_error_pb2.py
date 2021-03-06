# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/errors/feed_attribute_reference_error.proto

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
  name='google/ads/googleads_v0/proto/errors/feed_attribute_reference_error.proto',
  package='google.ads.googleads.v0.errors',
  syntax='proto3',
  serialized_pb=_b('\nIgoogle/ads/googleads_v0/proto/errors/feed_attribute_reference_error.proto\x12\x1egoogle.ads.googleads.v0.errors\"\xba\x01\n\x1f\x46\x65\x65\x64\x41ttributeReferenceErrorEnum\"\x96\x01\n\x1b\x46\x65\x65\x64\x41ttributeReferenceError\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12!\n\x1d\x43\x41NNOT_REFERENCE_DELETED_FEED\x10\x02\x12\x15\n\x11INVALID_FEED_NAME\x10\x03\x12\x1f\n\x1bINVALID_FEED_ATTRIBUTE_NAME\x10\x04\x42\xd6\x01\n\"com.google.ads.googleads.v0.errorsB FeedAttributeReferenceErrorProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V0.Errors\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V0\\Errorsb\x06proto3')
)



_FEEDATTRIBUTEREFERENCEERRORENUM_FEEDATTRIBUTEREFERENCEERROR = _descriptor.EnumDescriptor(
  name='FeedAttributeReferenceError',
  full_name='google.ads.googleads.v0.errors.FeedAttributeReferenceErrorEnum.FeedAttributeReferenceError',
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
      name='CANNOT_REFERENCE_DELETED_FEED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FEED_NAME', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_FEED_ATTRIBUTE_NAME', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=146,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_FEEDATTRIBUTEREFERENCEERRORENUM_FEEDATTRIBUTEREFERENCEERROR)


_FEEDATTRIBUTEREFERENCEERRORENUM = _descriptor.Descriptor(
  name='FeedAttributeReferenceErrorEnum',
  full_name='google.ads.googleads.v0.errors.FeedAttributeReferenceErrorEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FEEDATTRIBUTEREFERENCEERRORENUM_FEEDATTRIBUTEREFERENCEERROR,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=296,
)

_FEEDATTRIBUTEREFERENCEERRORENUM_FEEDATTRIBUTEREFERENCEERROR.containing_type = _FEEDATTRIBUTEREFERENCEERRORENUM
DESCRIPTOR.message_types_by_name['FeedAttributeReferenceErrorEnum'] = _FEEDATTRIBUTEREFERENCEERRORENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedAttributeReferenceErrorEnum = _reflection.GeneratedProtocolMessageType('FeedAttributeReferenceErrorEnum', (_message.Message,), dict(
  DESCRIPTOR = _FEEDATTRIBUTEREFERENCEERRORENUM,
  __module__ = 'google.ads.google_ads.v0.proto.errors.feed_attribute_reference_error_pb2'
  ,
  __doc__ = """Container for enum describing possible feed attribute reference errors.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.errors.FeedAttributeReferenceErrorEnum)
  ))
_sym_db.RegisterMessage(FeedAttributeReferenceErrorEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"com.google.ads.googleads.v0.errorsB FeedAttributeReferenceErrorProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v0/errors;errors\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V0.Errors\312\002\036Google\\Ads\\GoogleAds\\V0\\Errors'))
# @@protoc_insertion_point(module_scope)
