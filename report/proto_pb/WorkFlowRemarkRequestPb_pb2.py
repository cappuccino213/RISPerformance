# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorkFlowRemarkRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WorkFlowRemarkRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1dWorkFlowRemarkRequestPb.proto\"\xda\x02\n\x17WorkFlowRemarkRequestPb\x12\x12\n\nworkFlowID\x18\x01 \x01(\t\x12\x13\n\x0blinkOrderID\x18\x02 \x01(\t\x12\x16\n\x0eworkFlowStatus\x18\x03 \x01(\x05\x12\x19\n\x11\x61ttentionsContent\x18\x04 \x01(\t\x12\x17\n\x0f\x61ttentionsLevel\x18\x05 \x01(\t\x12\x17\n\x0fwriteRemarkDate\x18\x06 \x01(\t\x12\x19\n\x11writeRemarkUserID\x18\x07 \x01(\t\x12\x1b\n\x13writeRemarkUserName\x18\x08 \x01(\t\x12\x14\n\x0cworkFlowType\x18\t \x01(\x05\x12\x13\n\x0bprocessFlag\x18\n \x01(\x08\x12\x12\n\nisTempFlag\x18\x0b \x01(\x08\x12\x11\n\ttempTitle\x18\x0c \x01(\t\x12\x15\n\risHistoryData\x18\r \x01(\x08\x12\x10\n\x08medrecNo\x18\x0e \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_WORKFLOWREMARKREQUESTPB = _descriptor.Descriptor(
  name='WorkFlowRemarkRequestPb',
  full_name='WorkFlowRemarkRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workFlowID', full_name='WorkFlowRemarkRequestPb.workFlowID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkOrderID', full_name='WorkFlowRemarkRequestPb.linkOrderID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workFlowStatus', full_name='WorkFlowRemarkRequestPb.workFlowStatus', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attentionsContent', full_name='WorkFlowRemarkRequestPb.attentionsContent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attentionsLevel', full_name='WorkFlowRemarkRequestPb.attentionsLevel', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeRemarkDate', full_name='WorkFlowRemarkRequestPb.writeRemarkDate', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeRemarkUserID', full_name='WorkFlowRemarkRequestPb.writeRemarkUserID', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeRemarkUserName', full_name='WorkFlowRemarkRequestPb.writeRemarkUserName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workFlowType', full_name='WorkFlowRemarkRequestPb.workFlowType', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processFlag', full_name='WorkFlowRemarkRequestPb.processFlag', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isTempFlag', full_name='WorkFlowRemarkRequestPb.isTempFlag', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tempTitle', full_name='WorkFlowRemarkRequestPb.tempTitle', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isHistoryData', full_name='WorkFlowRemarkRequestPb.isHistoryData', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medrecNo', full_name='WorkFlowRemarkRequestPb.medrecNo', index=13,
      number=14, type=9, cpp_type=9, label=1,
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
  serialized_end=380,
)

DESCRIPTOR.message_types_by_name['WorkFlowRemarkRequestPb'] = _WORKFLOWREMARKREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkFlowRemarkRequestPb = _reflection.GeneratedProtocolMessageType('WorkFlowRemarkRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWREMARKREQUESTPB,
  '__module__' : 'WorkFlowRemarkRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:WorkFlowRemarkRequestPb)
  })
_sym_db.RegisterMessage(WorkFlowRemarkRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)