# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LocationExamineCountListResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import register.proto_pb.LocationExamineCountResponsePb_pb2 as LocationExamineCountResponsePb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='LocationExamineCountListResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n(LocationExamineCountListResponsePb.proto\x1a$LocationExamineCountResponsePb.proto\"c\n\"LocationExamineCountListResponsePb\x12=\n\x14locationExamineCount\x18\x01 \x03(\x0b\x32\x1f.LocationExamineCountResponsePbB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[LocationExamineCountResponsePb__pb2.DESCRIPTOR,])




_LOCATIONEXAMINECOUNTLISTRESPONSEPB = _descriptor.Descriptor(
  name='LocationExamineCountListResponsePb',
  full_name='LocationExamineCountListResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='locationExamineCount', full_name='LocationExamineCountListResponsePb.locationExamineCount', index=0,
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
  serialized_start=82,
  serialized_end=181,
)

_LOCATIONEXAMINECOUNTLISTRESPONSEPB.fields_by_name['locationExamineCount'].message_type = LocationExamineCountResponsePb__pb2._LOCATIONEXAMINECOUNTRESPONSEPB
DESCRIPTOR.message_types_by_name['LocationExamineCountListResponsePb'] = _LOCATIONEXAMINECOUNTLISTRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationExamineCountListResponsePb = _reflection.GeneratedProtocolMessageType('LocationExamineCountListResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONEXAMINECOUNTLISTRESPONSEPB,
  '__module__' : 'LocationExamineCountListResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:LocationExamineCountListResponsePb)
  })
_sym_db.RegisterMessage(LocationExamineCountListResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
