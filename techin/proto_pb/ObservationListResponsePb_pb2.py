# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ObservationListResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import techin.proto_pb.OrderResponsePb_pb2 as OrderResponsePb__pb2



DESCRIPTOR = _descriptor.FileDescriptor(
  name='ObservationListResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1fObservationListResponsePb.proto\x1a\x15OrderResponsePb.proto\"i\n\x19ObservationListResponsePb\x12&\n\x0cunFinishList\x18\x01 \x03(\x0b\x32\x10.OrderResponsePb\x12$\n\nhangUpList\x18\x02 \x03(\x0b\x32\x10.OrderResponsePbB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[OrderResponsePb__pb2.DESCRIPTOR,])




_OBSERVATIONLISTRESPONSEPB = _descriptor.Descriptor(
  name='ObservationListResponsePb',
  full_name='ObservationListResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unFinishList', full_name='ObservationListResponsePb.unFinishList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hangUpList', full_name='ObservationListResponsePb.hangUpList', index=1,
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
  serialized_start=58,
  serialized_end=163,
)

_OBSERVATIONLISTRESPONSEPB.fields_by_name['unFinishList'].message_type = OrderResponsePb__pb2._ORDERRESPONSEPB
_OBSERVATIONLISTRESPONSEPB.fields_by_name['hangUpList'].message_type = OrderResponsePb__pb2._ORDERRESPONSEPB
DESCRIPTOR.message_types_by_name['ObservationListResponsePb'] = _OBSERVATIONLISTRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObservationListResponsePb = _reflection.GeneratedProtocolMessageType('ObservationListResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONLISTRESPONSEPB,
  '__module__' : 'ObservationListResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ObservationListResponsePb)
  })
_sym_db.RegisterMessage(ObservationListResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
