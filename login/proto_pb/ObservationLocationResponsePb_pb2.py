# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ObservationLocationResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ObservationLocationResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n#ObservationLocationResponsePb.proto\"\xad\x05\n\x1dObservationLocationResponsePb\x12\x1d\n\x15observationLocationID\x18\x01 \x01(\t\x12\x1f\n\x17observationLocationCode\x18\x02 \x01(\t\x12\x1b\n\x13observationLocation\x18\x03 \x01(\t\x12\x0f\n\x07\x61\x45Title\x18\x04 \x01(\t\x12\x1b\n\x13observationPriority\x18\x05 \x01(\t\x12\x1d\n\x15observationPriorityCH\x18\x06 \x01(\t\x12\x14\n\x0clocationFlag\x18\x07 \x01(\t\x12\x16\n\x0elocationFlagCH\x18\x08 \x01(\t\x12\x1b\n\x13locationReserveName\x18\t \x01(\t\x12\x15\n\rserviceSectID\x18\n \x01(\t\x12\x15\n\rlinkQueueCode\x18\x0b \x01(\t\x12\x1b\n\x13virtualLocationFlag\x18\x0c \x01(\x08\x12\x1d\n\x15virtualLocationFlagCH\x18\r \x01(\t\x12\x19\n\x11\x64utyTechniciansID\x18\x0e \x01(\t\x12\x1b\n\x13\x64utyTechniciansName\x18\x0f \x01(\t\x12\x18\n\x10\x63\x61llNoLocationID\x18\x10 \x01(\t\x12\x19\n\x11observationDeptID\x18\x11 \x01(\t\x12\x1b\n\x13observationDeptName\x18\x12 \x01(\t\x12\x16\n\x0eorganizationID\x18\x13 \x01(\t\x12\x18\n\x10organizationName\x18\x14 \x01(\t\x12\x13\n\x0b\x64\x65letedFlag\x18\x15 \x01(\x08\x12\x14\n\x0c\x64\x65leteFlagCH\x18\x16 \x01(\t\x12\x0e\n\x06remark\x18\x17 \x01(\t\x12\x0e\n\x06sortNo\x18\x18 \x01(\x05\x12\x14\n\x0cuncheckedNum\x18\x19 \x01(\x05\x12\x10\n\x08totalNum\x18\x1a \x01(\x05\x42\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_OBSERVATIONLOCATIONRESPONSEPB = _descriptor.Descriptor(
  name='ObservationLocationResponsePb',
  full_name='ObservationLocationResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observationLocationID', full_name='ObservationLocationResponsePb.observationLocationID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationLocationCode', full_name='ObservationLocationResponsePb.observationLocationCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationLocation', full_name='ObservationLocationResponsePb.observationLocation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aETitle', full_name='ObservationLocationResponsePb.aETitle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationPriority', full_name='ObservationLocationResponsePb.observationPriority', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationPriorityCH', full_name='ObservationLocationResponsePb.observationPriorityCH', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locationFlag', full_name='ObservationLocationResponsePb.locationFlag', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locationFlagCH', full_name='ObservationLocationResponsePb.locationFlagCH', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locationReserveName', full_name='ObservationLocationResponsePb.locationReserveName', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='ObservationLocationResponsePb.serviceSectID', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkQueueCode', full_name='ObservationLocationResponsePb.linkQueueCode', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='virtualLocationFlag', full_name='ObservationLocationResponsePb.virtualLocationFlag', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='virtualLocationFlagCH', full_name='ObservationLocationResponsePb.virtualLocationFlagCH', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dutyTechniciansID', full_name='ObservationLocationResponsePb.dutyTechniciansID', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dutyTechniciansName', full_name='ObservationLocationResponsePb.dutyTechniciansName', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callNoLocationID', full_name='ObservationLocationResponsePb.callNoLocationID', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationDeptID', full_name='ObservationLocationResponsePb.observationDeptID', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationDeptName', full_name='ObservationLocationResponsePb.observationDeptName', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='ObservationLocationResponsePb.organizationID', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationName', full_name='ObservationLocationResponsePb.organizationName', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deletedFlag', full_name='ObservationLocationResponsePb.deletedFlag', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleteFlagCH', full_name='ObservationLocationResponsePb.deleteFlagCH', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remark', full_name='ObservationLocationResponsePb.remark', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sortNo', full_name='ObservationLocationResponsePb.sortNo', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uncheckedNum', full_name='ObservationLocationResponsePb.uncheckedNum', index=24,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='totalNum', full_name='ObservationLocationResponsePb.totalNum', index=25,
      number=26, type=5, cpp_type=1, label=1,
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
  serialized_start=40,
  serialized_end=725,
)

DESCRIPTOR.message_types_by_name['ObservationLocationResponsePb'] = _OBSERVATIONLOCATIONRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ObservationLocationResponsePb = _reflection.GeneratedProtocolMessageType('ObservationLocationResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _OBSERVATIONLOCATIONRESPONSEPB,
  '__module__' : 'ObservationLocationResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ObservationLocationResponsePb)
  })
_sym_db.RegisterMessage(ObservationLocationResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
