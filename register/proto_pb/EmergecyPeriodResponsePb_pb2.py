# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EmergecyPeriodResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='EmergecyPeriodResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1e\x45mergecyPeriodResponsePb.proto\"S\n\x18\x45mergecyPeriodResponsePb\x12\x13\n\x0bparameterID\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_EMERGECYPERIODRESPONSEPB = _descriptor.Descriptor(
  name='EmergecyPeriodResponsePb',
  full_name='EmergecyPeriodResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameterID', full_name='EmergecyPeriodResponsePb.parameterID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startTime', full_name='EmergecyPeriodResponsePb.startTime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='EmergecyPeriodResponsePb.endTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=34,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['EmergecyPeriodResponsePb'] = _EMERGECYPERIODRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmergecyPeriodResponsePb = _reflection.GeneratedProtocolMessageType('EmergecyPeriodResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _EMERGECYPERIODRESPONSEPB,
  '__module__' : 'EmergecyPeriodResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:EmergecyPeriodResponsePb)
  })
_sym_db.RegisterMessage(EmergecyPeriodResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
