# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='MessageRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x16MessageRequestPb.proto\"\x9d\x01\n\x10MessageRequestPb\x12\x11\n\tparamName\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x02 \x01(\t\x12\x12\n\nmsgContent\x18\x03 \x01(\t\x12\x15\n\rmsgBoxButtons\x18\x04 \x01(\t\x12\x13\n\x0bmsgBoxIcons\x18\x05 \x01(\t\x12\x11\n\tmsgResult\x18\x06 \x01(\t\x12\x12\n\nisFinished\x18\x07 \x01(\x08\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_MESSAGEREQUESTPB = _descriptor.Descriptor(
  name='MessageRequestPb',
  full_name='MessageRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paramName', full_name='MessageRequestPb.paramName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='caption', full_name='MessageRequestPb.caption', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgContent', full_name='MessageRequestPb.msgContent', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgBoxButtons', full_name='MessageRequestPb.msgBoxButtons', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgBoxIcons', full_name='MessageRequestPb.msgBoxIcons', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msgResult', full_name='MessageRequestPb.msgResult', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isFinished', full_name='MessageRequestPb.isFinished', index=6,
      number=7, type=8, cpp_type=7, label=1,
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
  serialized_start=27,
  serialized_end=184,
)

DESCRIPTOR.message_types_by_name['MessageRequestPb'] = _MESSAGEREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageRequestPb = _reflection.GeneratedProtocolMessageType('MessageRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEREQUESTPB,
  '__module__' : 'MessageRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:MessageRequestPb)
  })
_sym_db.RegisterMessage(MessageRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
