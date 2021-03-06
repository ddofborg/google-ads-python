# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/resources/carrier_constant.proto

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
  name='google/ads/googleads_v0/proto/resources/carrier_constant.proto',
  package='google.ads.googleads.v0.resources',
  syntax='proto3',
  serialized_pb=_b('\n>google/ads/googleads_v0/proto/resources/carrier_constant.proto\x12!google.ads.googleads.v0.resources\x1a\x1egoogle/protobuf/wrappers.proto\"\xb1\x01\n\x0f\x43\x61rrierConstant\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\'\n\x02id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x63ountry_code\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\xd9\x01\n%com.google.ads.googleads.v0.resourcesB\x14\x43\x61rrierConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V0.Resources\xca\x02!Google\\Ads\\GoogleAds\\V0\\Resourcesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_CARRIERCONSTANT = _descriptor.Descriptor(
  name='CarrierConstant',
  full_name='google.ads.googleads.v0.resources.CarrierConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v0.resources.CarrierConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v0.resources.CarrierConstant.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v0.resources.CarrierConstant.name', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='google.ads.googleads.v0.resources.CarrierConstant.country_code', index=3,
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
  serialized_start=134,
  serialized_end=311,
)

_CARRIERCONSTANT.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_CARRIERCONSTANT.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CARRIERCONSTANT.fields_by_name['country_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['CarrierConstant'] = _CARRIERCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarrierConstant = _reflection.GeneratedProtocolMessageType('CarrierConstant', (_message.Message,), dict(
  DESCRIPTOR = _CARRIERCONSTANT,
  __module__ = 'google.ads.google_ads.v0.proto.resources.carrier_constant_pb2'
  ,
  __doc__ = """A carrier criterion that can be used in campaign targeting.
  
  
  Attributes:
      resource_name:
          The resource name of the carrier criterion. Carrier criterion
          resource names have the form:
          ``carrierConstants/{criterion_id}``
      id:
          The ID of the carrier criterion.
      name:
          The full name of the carrier in English.
      country_code:
          The country code of the country where the carrier is located,
          e.g., "AR", "FR", etc.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.resources.CarrierConstant)
  ))
_sym_db.RegisterMessage(CarrierConstant)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n%com.google.ads.googleads.v0.resourcesB\024CarrierConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v0/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V0.Resources\312\002!Google\\Ads\\GoogleAds\\V0\\Resources'))
# @@protoc_insertion_point(module_scope)
