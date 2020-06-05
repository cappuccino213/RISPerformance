# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WorkFlowRemarkResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WorkFlowRemarkResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1eWorkFlowRemarkResponsePb.proto\"\xd7\x02\n\x18WorkFlowRemarkResponsePb\x12\x12\n\nworkFlowID\x18\x01 \x01(\t\x12\x13\n\x0blinkOrderID\x18\x02 \x01(\t\x12\x16\n\x0eworkFlowStatus\x18\x03 \x01(\t\x12\x19\n\x11\x61ttentionsContent\x18\x04 \x01(\t\x12\x17\n\x0f\x61ttentionsLevel\x18\x05 \x01(\t\x12\x17\n\x0fwriteRemarkDate\x18\x06 \x01(\t\x12\x19\n\x11writeRemarkUserID\x18\x07 \x01(\t\x12\x1b\n\x13writeRemarkUserName\x18\x08 \x01(\t\x12\x14\n\x0cworkFlowType\x18\t \x01(\t\x12\x13\n\x0bprocessFlag\x18\n \x01(\x08\x12\x15\n\risHistoryData\x18\x0b \x01(\x08\x12\x19\n\x11\x61ttentionsLevelCH\x18\x0c \x01(\t\x12\x18\n\x10workFlowStatusCH\x18\r \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_WORKFLOWREMARKRESPONSEPB = _descriptor.Descriptor(
  name='WorkFlowRemarkResponsePb',
  full_name='WorkFlowRemarkResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workFlowID', full_name='WorkFlowRemarkResponsePb.workFlowID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linkOrderID', full_name='WorkFlowRemarkResponsePb.linkOrderID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workFlowStatus', full_name='WorkFlowRemarkResponsePb.workFlowStatus', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attentionsContent', full_name='WorkFlowRemarkResponsePb.attentionsContent', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attentionsLevel', full_name='WorkFlowRemarkResponsePb.attentionsLevel', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeRemarkDate', full_name='WorkFlowRemarkResponsePb.writeRemarkDate', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeRemarkUserID', full_name='WorkFlowRemarkResponsePb.writeRemarkUserID', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeRemarkUserName', full_name='WorkFlowRemarkResponsePb.writeRemarkUserName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workFlowType', full_name='WorkFlowRemarkResponsePb.workFlowType', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='processFlag', full_name='WorkFlowRemarkResponsePb.processFlag', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isHistoryData', full_name='WorkFlowRemarkResponsePb.isHistoryData', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attentionsLevelCH', full_name='WorkFlowRemarkResponsePb.attentionsLevelCH', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workFlowStatusCH', full_name='WorkFlowRemarkResponsePb.workFlowStatusCH', index=12,
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
  serialized_start=35,
  serialized_end=378,
)

DESCRIPTOR.message_types_by_name['WorkFlowRemarkResponsePb'] = _WORKFLOWREMARKRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorkFlowRemarkResponsePb = _reflection.GeneratedProtocolMessageType('WorkFlowRemarkResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _WORKFLOWREMARKRESPONSEPB,
  '__module__' : 'WorkFlowRemarkResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:WorkFlowRemarkResponsePb)
  })
_sym_db.RegisterMessage(WorkFlowRemarkResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
