# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: LocationExamineCountResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='LocationExamineCountResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n$LocationExamineCountResponsePb.proto\"\x98\x02\n\x1eLocationExamineCountResponsePb\x12\x1d\n\x15observationLocationID\x18\x01 \x01(\t\x12\x1f\n\x17observationLocationCode\x18\x02 \x01(\t\x12\x1b\n\x13observationLocation\x18\x03 \x01(\t\x12\x14\n\x0clocationFlag\x18\x04 \x01(\t\x12\x12\n\ntotalCount\x18\x05 \x01(\x05\x12\x17\n\x0fregisteredCount\x18\x06 \x01(\x05\x12\x14\n\x0c\x63heckedCount\x18\x07 \x01(\x05\x12\x18\n\x10waitToCheckCount\x18\x08 \x01(\x05\x12\x0f\n\x07\x63harges\x18\t \x01(\x02\x12\x15\n\rserviceSectID\x18\n \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_LOCATIONEXAMINECOUNTRESPONSEPB = _descriptor.Descriptor(
  name='LocationExamineCountResponsePb',
  full_name='LocationExamineCountResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observationLocationID', full_name='LocationExamineCountResponsePb.observationLocationID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationLocationCode', full_name='LocationExamineCountResponsePb.observationLocationCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationLocation', full_name='LocationExamineCountResponsePb.observationLocation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locationFlag', full_name='LocationExamineCountResponsePb.locationFlag', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalCount', full_name='LocationExamineCountResponsePb.totalCount', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registeredCount', full_name='LocationExamineCountResponsePb.registeredCount', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkedCount', full_name='LocationExamineCountResponsePb.checkedCount', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waitToCheckCount', full_name='LocationExamineCountResponsePb.waitToCheckCount', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charges', full_name='LocationExamineCountResponsePb.charges', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='LocationExamineCountResponsePb.serviceSectID', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=41,
  serialized_end=321,
)

DESCRIPTOR.message_types_by_name['LocationExamineCountResponsePb'] = _LOCATIONEXAMINECOUNTRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationExamineCountResponsePb = _reflection.GeneratedProtocolMessageType('LocationExamineCountResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONEXAMINECOUNTRESPONSEPB,
  '__module__' : 'LocationExamineCountResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:LocationExamineCountResponsePb)
  })
_sym_db.RegisterMessage(LocationExamineCountResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
