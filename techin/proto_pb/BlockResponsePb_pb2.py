# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BlockResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='BlockResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x15\x42lockResponsePb.proto\"\xb4\x02\n\x0f\x42lockResponsePb\x12\x15\n\rworkQueueGuid\x18\x01 \x01(\t\x12\x11\n\tpatientId\x18\x02 \x01(\t\x12\x13\n\x0bpatientName\x18\x03 \x01(\t\x12\x11\n\totherName\x18\x04 \x01(\t\x12\x12\n\npatientAge\x18\x05 \x01(\t\x12\x17\n\x0fpatientBirthday\x18\x06 \x01(\t\x12\x12\n\npatientSex\x18\x07 \x01(\t\x12\x10\n\x08modality\x18\x08 \x01(\t\x12\x15\n\rstudyDateTime\x18\t \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\n \x01(\t\x12\x18\n\x10studyInstanceUID\x18\x0b \x01(\t\x12\x18\n\x10studyDescription\x18\x0c \x01(\t\x12\x18\n\x10organizationCode\x18\r \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_BLOCKRESPONSEPB = _descriptor.Descriptor(
  name='BlockResponsePb',
  full_name='BlockResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workQueueGuid', full_name='BlockResponsePb.workQueueGuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientId', full_name='BlockResponsePb.patientId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientName', full_name='BlockResponsePb.patientName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='otherName', full_name='BlockResponsePb.otherName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientAge', full_name='BlockResponsePb.patientAge', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientBirthday', full_name='BlockResponsePb.patientBirthday', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientSex', full_name='BlockResponsePb.patientSex', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='modality', full_name='BlockResponsePb.modality', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='studyDateTime', full_name='BlockResponsePb.studyDateTime', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='BlockResponsePb.accessionNumber', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='studyInstanceUID', full_name='BlockResponsePb.studyInstanceUID', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='studyDescription', full_name='BlockResponsePb.studyDescription', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationCode', full_name='BlockResponsePb.organizationCode', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=334,
)

DESCRIPTOR.message_types_by_name['BlockResponsePb'] = _BLOCKRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BlockResponsePb = _reflection.GeneratedProtocolMessageType('BlockResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKRESPONSEPB,
  '__module__' : 'BlockResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:BlockResponsePb)
  })
_sym_db.RegisterMessage(BlockResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
