# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FinishExamResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import techin.proto_pb.MessageResponsePb_pb2 as MessageResponsePb__pb2
import techin.proto_pb.CommonPrintFileResponsePb_pb2 as CommonPrintFileResponsePb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='FinishExamResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1a\x46inishExamResponsePb.proto\x1a\x17MessageResponsePb.proto\x1a\x1f\x43ommonPrintFileResponsePb.proto\"l\n\x14\x46inishExamResponsePb\x12.\n\nprintFiles\x18\x01 \x03(\x0b\x32\x1a.CommonPrintFileResponsePb\x12$\n\x08messages\x18\x02 \x03(\x0b\x32\x12.MessageResponsePbB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[MessageResponsePb__pb2.DESCRIPTOR,CommonPrintFileResponsePb__pb2.DESCRIPTOR,])




_FINISHEXAMRESPONSEPB = _descriptor.Descriptor(
  name='FinishExamResponsePb',
  full_name='FinishExamResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='printFiles', full_name='FinishExamResponsePb.printFiles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messages', full_name='FinishExamResponsePb.messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=88,
  serialized_end=196,
)

_FINISHEXAMRESPONSEPB.fields_by_name['printFiles'].message_type = CommonPrintFileResponsePb__pb2._COMMONPRINTFILERESPONSEPB
_FINISHEXAMRESPONSEPB.fields_by_name['messages'].message_type = MessageResponsePb__pb2._MESSAGERESPONSEPB
DESCRIPTOR.message_types_by_name['FinishExamResponsePb'] = _FINISHEXAMRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FinishExamResponsePb = _reflection.GeneratedProtocolMessageType('FinishExamResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _FINISHEXAMRESPONSEPB,
  '__module__' : 'FinishExamResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:FinishExamResponsePb)
  })
_sym_db.RegisterMessage(FinishExamResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
