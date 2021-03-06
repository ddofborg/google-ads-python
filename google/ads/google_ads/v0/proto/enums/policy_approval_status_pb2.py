# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v0/proto/enums/policy_approval_status.proto

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
  name='google/ads/googleads_v0/proto/enums/policy_approval_status.proto',
  package='google.ads.googleads.v0.enums',
  syntax='proto3',
  serialized_pb=_b('\n@google/ads/googleads_v0/proto/enums/policy_approval_status.proto\x12\x1dgoogle.ads.googleads.v0.enums\"\xa1\x01\n\x18PolicyApprovalStatusEnum\"\x84\x01\n\x14PolicyApprovalStatus\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0f\n\x0b\x44ISAPPROVED\x10\x02\x12\x14\n\x10\x41PPROVED_LIMITED\x10\x03\x12\x0c\n\x08\x41PPROVED\x10\x04\x12\x19\n\x15\x41REA_OF_INTEREST_ONLY\x10\x05\x42\xca\x01\n!com.google.ads.googleads.v0.enumsB\x19PolicyApprovalStatusProtoP\x01ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\xa2\x02\x03GAA\xaa\x02\x1dGoogle.Ads.GoogleAds.V0.Enums\xca\x02\x1dGoogle\\Ads\\GoogleAds\\V0\\Enumsb\x06proto3')
)



_POLICYAPPROVALSTATUSENUM_POLICYAPPROVALSTATUS = _descriptor.EnumDescriptor(
  name='PolicyApprovalStatus',
  full_name='google.ads.googleads.v0.enums.PolicyApprovalStatusEnum.PolicyApprovalStatus',
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
      name='DISAPPROVED', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED_LIMITED', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVED', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AREA_OF_INTEREST_ONLY', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=129,
  serialized_end=261,
)
_sym_db.RegisterEnumDescriptor(_POLICYAPPROVALSTATUSENUM_POLICYAPPROVALSTATUS)


_POLICYAPPROVALSTATUSENUM = _descriptor.Descriptor(
  name='PolicyApprovalStatusEnum',
  full_name='google.ads.googleads.v0.enums.PolicyApprovalStatusEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _POLICYAPPROVALSTATUSENUM_POLICYAPPROVALSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=261,
)

_POLICYAPPROVALSTATUSENUM_POLICYAPPROVALSTATUS.containing_type = _POLICYAPPROVALSTATUSENUM
DESCRIPTOR.message_types_by_name['PolicyApprovalStatusEnum'] = _POLICYAPPROVALSTATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PolicyApprovalStatusEnum = _reflection.GeneratedProtocolMessageType('PolicyApprovalStatusEnum', (_message.Message,), dict(
  DESCRIPTOR = _POLICYAPPROVALSTATUSENUM,
  __module__ = 'google.ads.google_ads.v0.proto.enums.policy_approval_status_pb2'
  ,
  __doc__ = """Container for enum describing possible policy approval statuses.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v0.enums.PolicyApprovalStatusEnum)
  ))
_sym_db.RegisterMessage(PolicyApprovalStatusEnum)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.ads.googleads.v0.enumsB\031PolicyApprovalStatusProtoP\001ZBgoogle.golang.org/genproto/googleapis/ads/googleads/v0/enums;enums\242\002\003GAA\252\002\035Google.Ads.GoogleAds.V0.Enums\312\002\035Google\\Ads\\GoogleAds\\V0\\Enums'))
# @@protoc_insertion_point(module_scope)
