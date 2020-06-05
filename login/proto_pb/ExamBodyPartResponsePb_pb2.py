# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ExamBodyPartResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ExamBodyPartResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1c\x45xamBodyPartResponsePb.proto\"\xc4\x02\n\x16\x45xamBodyPartResponsePb\x12\x16\n\x0e\x65xamBodyPartID\x18\x01 \x01(\t\x12\x18\n\x10\x65xamBodyPartCode\x18\x02 \x01(\t\x12\x11\n\tinPutCode\x18\x03 \x01(\t\x12\x18\n\x10\x65xamBodyPartName\x18\x04 \x01(\t\x12\x17\n\x0f\x65xamBodyPartEng\x18\x05 \x01(\t\x12\x15\n\rserviceSectID\x18\x06 \x01(\t\x12\x14\n\x0cphysicalFlag\x18\x07 \x01(\x08\x12\x16\n\x0ephysicalFlagCH\x18\x08 \x01(\t\x12\x19\n\x11observationDeptID\x18\t \x01(\t\x12\x16\n\x0eorganizationID\x18\n \x01(\t\x12\x13\n\x0b\x64\x65letedFlag\x18\x0b \x01(\x08\x12\x15\n\rdeletedFlagCH\x18\x0c \x01(\t\x12\x0e\n\x06sortNO\x18\r \x01(\x05\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_EXAMBODYPARTRESPONSEPB = _descriptor.Descriptor(
  name='ExamBodyPartResponsePb',
  full_name='ExamBodyPartResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='examBodyPartID', full_name='ExamBodyPartResponsePb.examBodyPartID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examBodyPartCode', full_name='ExamBodyPartResponsePb.examBodyPartCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inPutCode', full_name='ExamBodyPartResponsePb.inPutCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examBodyPartName', full_name='ExamBodyPartResponsePb.examBodyPartName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examBodyPartEng', full_name='ExamBodyPartResponsePb.examBodyPartEng', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='ExamBodyPartResponsePb.serviceSectID', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physicalFlag', full_name='ExamBodyPartResponsePb.physicalFlag', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physicalFlagCH', full_name='ExamBodyPartResponsePb.physicalFlagCH', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationDeptID', full_name='ExamBodyPartResponsePb.observationDeptID', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='ExamBodyPartResponsePb.organizationID', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deletedFlag', full_name='ExamBodyPartResponsePb.deletedFlag', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deletedFlagCH', full_name='ExamBodyPartResponsePb.deletedFlagCH', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sortNO', full_name='ExamBodyPartResponsePb.sortNO', index=12,
      number=13, type=5, cpp_type=1, label=1,
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
  serialized_start=33,
  serialized_end=357,
)

DESCRIPTOR.message_types_by_name['ExamBodyPartResponsePb'] = _EXAMBODYPARTRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExamBodyPartResponsePb = _reflection.GeneratedProtocolMessageType('ExamBodyPartResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _EXAMBODYPARTRESPONSEPB,
  '__module__' : 'ExamBodyPartResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ExamBodyPartResponsePb)
  })
_sym_db.RegisterMessage(ExamBodyPartResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
