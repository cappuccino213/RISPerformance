# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PatientClassResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='PatientClassResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1cPatientClassResponsePb.proto\"\xb4\x02\n\x16PatientClassResponsePb\x12\x0c\n\x04pKID\x18\x01 \x01(\t\x12\x18\n\x10patientClassName\x18\x02 \x01(\t\x12\x18\n\x10patientClassCode\x18\x03 \x01(\t\x12\x1b\n\x13patientClassNameEng\x18\x04 \x01(\t\x12\x0f\n\x07hISCode\x18\x05 \x01(\t\x12\x12\n\ncolorValue\x18\x06 \x01(\t\x12\x17\n\x0fparentClassCode\x18\x07 \x01(\x05\x12\x0e\n\x06remark\x18\x08 \x01(\t\x12\x19\n\x11observationDeptID\x18\t \x01(\t\x12\x16\n\x0eorganizationID\x18\n \x01(\t\x12\x15\n\ractivatedFlag\x18\x0b \x01(\x08\x12\x13\n\x0b\x64\x65letedFlag\x18\x0c \x01(\x08\x12\x0e\n\x06sortNo\x18\r \x01(\x05\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_PATIENTCLASSRESPONSEPB = _descriptor.Descriptor(
  name='PatientClassResponsePb',
  full_name='PatientClassResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pKID', full_name='PatientClassResponsePb.pKID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientClassName', full_name='PatientClassResponsePb.patientClassName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientClassCode', full_name='PatientClassResponsePb.patientClassCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientClassNameEng', full_name='PatientClassResponsePb.patientClassNameEng', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hISCode', full_name='PatientClassResponsePb.hISCode', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='colorValue', full_name='PatientClassResponsePb.colorValue', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parentClassCode', full_name='PatientClassResponsePb.parentClassCode', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remark', full_name='PatientClassResponsePb.remark', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationDeptID', full_name='PatientClassResponsePb.observationDeptID', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='PatientClassResponsePb.organizationID', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activatedFlag', full_name='PatientClassResponsePb.activatedFlag', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deletedFlag', full_name='PatientClassResponsePb.deletedFlag', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sortNo', full_name='PatientClassResponsePb.sortNo', index=12,
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
  serialized_end=341,
)

DESCRIPTOR.message_types_by_name['PatientClassResponsePb'] = _PATIENTCLASSRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PatientClassResponsePb = _reflection.GeneratedProtocolMessageType('PatientClassResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _PATIENTCLASSRESPONSEPB,
  '__module__' : 'PatientClassResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:PatientClassResponsePb)
  })
_sym_db.RegisterMessage(PatientClassResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
