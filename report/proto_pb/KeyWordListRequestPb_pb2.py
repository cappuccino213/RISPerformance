# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KeyWordListRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import KeyWordRequestPb_pb2 as KeyWordRequestPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='KeyWordListRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1aKeyWordListRequestPb.proto\x1a\x16KeyWordRequestPb.proto\"7\n\x14KeyWordListRequestPb\x12\x1f\n\x04list\x18\x01 \x03(\x0b\x32\x11.KeyWordRequestPbB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[KeyWordRequestPb__pb2.DESCRIPTOR,])




_KEYWORDLISTREQUESTPB = _descriptor.Descriptor(
  name='KeyWordListRequestPb',
  full_name='KeyWordListRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='KeyWordListRequestPb.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=54,
  serialized_end=109,
)

_KEYWORDLISTREQUESTPB.fields_by_name['list'].message_type = KeyWordRequestPb__pb2._KEYWORDREQUESTPB
DESCRIPTOR.message_types_by_name['KeyWordListRequestPb'] = _KEYWORDLISTREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KeyWordListRequestPb = _reflection.GeneratedProtocolMessageType('KeyWordListRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _KEYWORDLISTREQUESTPB,
  '__module__' : 'KeyWordListRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:KeyWordListRequestPb)
  })
_sym_db.RegisterMessage(KeyWordListRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
