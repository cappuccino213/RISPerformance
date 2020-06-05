# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OrderCancelRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='OrderCancelRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1aOrderCancelRequestPb.proto\"k\n\x14OrderCancelRequestPb\x12\x11\n\torderPKID\x18\x01 \x01(\t\x12\x0f\n\x07orderID\x18\x02 \x01(\t\x12\x14\n\x0c\x63\x61ncelReason\x18\x03 \x01(\t\x12\x19\n\x11isTechnicalCancel\x18\x04 \x01(\x08\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_ORDERCANCELREQUESTPB = _descriptor.Descriptor(
  name='OrderCancelRequestPb',
  full_name='OrderCancelRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderPKID', full_name='OrderCancelRequestPb.orderPKID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderID', full_name='OrderCancelRequestPb.orderID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cancelReason', full_name='OrderCancelRequestPb.cancelReason', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isTechnicalCancel', full_name='OrderCancelRequestPb.isTechnicalCancel', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=30,
  serialized_end=137,
)

DESCRIPTOR.message_types_by_name['OrderCancelRequestPb'] = _ORDERCANCELREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderCancelRequestPb = _reflection.GeneratedProtocolMessageType('OrderCancelRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _ORDERCANCELREQUESTPB,
  '__module__' : 'OrderCancelRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:OrderCancelRequestPb)
  })
_sym_db.RegisterMessage(OrderCancelRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)