# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CommonTypeRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='CommonTypeRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x19\x43ommonTypeRequestPb.proto\"\xbb\x01\n\x13\x43ommonTypeRequestPb\x12\x11\n\tparamType\x18\x01 \x01(\t\x12\x16\n\x0eorganizationID\x18\x02 \x03(\t\x12\x19\n\x11observationDeptID\x18\x03 \x03(\t\x12\x13\n\x0b\x63urrentPage\x18\x04 \x01(\x05\x12\x10\n\x08pageSize\x18\x05 \x01(\x05\x12\x10\n\x08userName\x18\x06 \x01(\t\x12\x10\n\x08userCode\x18\x07 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x08 \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_COMMONTYPEREQUESTPB = _descriptor.Descriptor(
  name='CommonTypeRequestPb',
  full_name='CommonTypeRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paramType', full_name='CommonTypeRequestPb.paramType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='CommonTypeRequestPb.organizationID', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationDeptID', full_name='CommonTypeRequestPb.observationDeptID', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='CommonTypeRequestPb.currentPage', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='CommonTypeRequestPb.pageSize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userName', full_name='CommonTypeRequestPb.userName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userCode', full_name='CommonTypeRequestPb.userCode', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accountName', full_name='CommonTypeRequestPb.accountName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=30,
  serialized_end=217,
)

DESCRIPTOR.message_types_by_name['CommonTypeRequestPb'] = _COMMONTYPEREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonTypeRequestPb = _reflection.GeneratedProtocolMessageType('CommonTypeRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _COMMONTYPEREQUESTPB,
  '__module__' : 'CommonTypeRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:CommonTypeRequestPb)
  })
_sym_db.RegisterMessage(CommonTypeRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
