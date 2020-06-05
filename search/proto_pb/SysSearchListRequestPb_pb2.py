# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SysSearchListRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import search.proto_pb.SysSearchDetailRequestPb_pb2 as SysSearchDetailRequestPb__pb2
import search.proto_pb.SysSearchSolutionRequestPb_pb2 as SysSearchSolutionRequestPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SysSearchListRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1cSysSearchListRequestPb.proto\x1a\x1eSysSearchDetailRequestPb.proto\x1a SysSearchSolutionRequestPb.proto\"\x9a\x01\n\x16SysSearchListRequestPb\x12*\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x19.SysSearchDetailRequestPb\x12-\n\x08solution\x18\x02 \x01(\x0b\x32\x1b.SysSearchSolutionRequestPb\x12\x13\n\x0b\x63urrentPage\x18\x03 \x01(\x05\x12\x10\n\x08pageSize\x18\x04 \x01(\x05\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[SysSearchDetailRequestPb__pb2.DESCRIPTOR,SysSearchSolutionRequestPb__pb2.DESCRIPTOR,])




_SYSSEARCHLISTREQUESTPB = _descriptor.Descriptor(
  name='SysSearchListRequestPb',
  full_name='SysSearchListRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='SysSearchListRequestPb.details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='solution', full_name='SysSearchListRequestPb.solution', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='SysSearchListRequestPb.currentPage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='SysSearchListRequestPb.pageSize', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=99,
  serialized_end=253,
)

_SYSSEARCHLISTREQUESTPB.fields_by_name['details'].message_type = SysSearchDetailRequestPb__pb2._SYSSEARCHDETAILREQUESTPB
_SYSSEARCHLISTREQUESTPB.fields_by_name['solution'].message_type = SysSearchSolutionRequestPb__pb2._SYSSEARCHSOLUTIONREQUESTPB
DESCRIPTOR.message_types_by_name['SysSearchListRequestPb'] = _SYSSEARCHLISTREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SysSearchListRequestPb = _reflection.GeneratedProtocolMessageType('SysSearchListRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _SYSSEARCHLISTREQUESTPB,
  '__module__' : 'SysSearchListRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:SysSearchListRequestPb)
  })
_sym_db.RegisterMessage(SysSearchListRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
