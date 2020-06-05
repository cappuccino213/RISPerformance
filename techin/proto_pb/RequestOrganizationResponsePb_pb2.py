# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RequestOrganizationResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RequestOrganizationResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n#RequestOrganizationResponsePb.proto\"\x96\x02\n\x1dRequestOrganizationResponsePb\x12\x14\n\x0crequestOrgID\x18\x01 \x01(\t\x12\x16\n\x0erequestOrgCode\x18\x02 \x01(\t\x12\x19\n\x11requestOrgHISCode\x18\x03 \x01(\t\x12\x16\n\x0erequestOrgName\x18\x04 \x01(\t\x12\x15\n\rrequestOrgEng\x18\x05 \x01(\t\x12\x11\n\tlinkOrgID\x18\x06 \x01(\t\x12\x19\n\x11ownOrganizationID\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65letedFlag\x18\x08 \x01(\x08\x12\x1a\n\x12\x64iagnoseCenterFlag\x18\n \x01(\x08\x12\x0e\n\x06remark\x18\x0b \x01(\t\x12\x0e\n\x06sortNo\x18\x0c \x01(\x05\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_REQUESTORGANIZATIONRESPONSEPB = _descriptor.Descriptor(
  name='RequestOrganizationResponsePb',
  full_name='RequestOrganizationResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestOrgID', full_name='RequestOrganizationResponsePb.requestOrgID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestOrgCode', full_name='RequestOrganizationResponsePb.requestOrgCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestOrgHISCode', full_name='RequestOrganizationResponsePb.requestOrgHISCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestOrgName', full_name='RequestOrganizationResponsePb.requestOrgName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestOrgEng', full_name='RequestOrganizationResponsePb.requestOrgEng', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkOrgID', full_name='RequestOrganizationResponsePb.linkOrgID', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ownOrganizationID', full_name='RequestOrganizationResponsePb.ownOrganizationID', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deletedFlag', full_name='RequestOrganizationResponsePb.deletedFlag', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diagnoseCenterFlag', full_name='RequestOrganizationResponsePb.diagnoseCenterFlag', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remark', full_name='RequestOrganizationResponsePb.remark', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sortNo', full_name='RequestOrganizationResponsePb.sortNo', index=10,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=40,
  serialized_end=318,
)

DESCRIPTOR.message_types_by_name['RequestOrganizationResponsePb'] = _REQUESTORGANIZATIONRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestOrganizationResponsePb = _reflection.GeneratedProtocolMessageType('RequestOrganizationResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTORGANIZATIONRESPONSEPB,
  '__module__' : 'RequestOrganizationResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:RequestOrganizationResponsePb)
  })
_sym_db.RegisterMessage(RequestOrganizationResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)