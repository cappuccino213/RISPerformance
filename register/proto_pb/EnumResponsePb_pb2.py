# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EnumResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='EnumResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x14\x45numResponsePb.proto\"N\n\x0e\x45numResponsePb\x12\x17\n\x0f\x64icDisplayValue\x18\x01 \x01(\t\x12\x0f\n\x07\x64icCode\x18\x02 \x01(\t\x12\x12\n\nisSelected\x18\x03 \x01(\x08\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_ENUMRESPONSEPB = _descriptor.Descriptor(
  name='EnumResponsePb',
  full_name='EnumResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dicDisplayValue', full_name='EnumResponsePb.dicDisplayValue', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dicCode', full_name='EnumResponsePb.dicCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isSelected', full_name='EnumResponsePb.isSelected', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=24,
  serialized_end=102,
)

DESCRIPTOR.message_types_by_name['EnumResponsePb'] = _ENUMRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnumResponsePb = _reflection.GeneratedProtocolMessageType('EnumResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _ENUMRESPONSEPB,
  '__module__' : 'EnumResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:EnumResponsePb)
  })
_sym_db.RegisterMessage(EnumResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
