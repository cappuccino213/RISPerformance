# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ImageViewRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ImageViewRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x18ImageViewRequestPb.proto\"%\n\x12ImageViewRequestPb\x12\x0f\n\x07orderID\x18\x01 \x03(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_IMAGEVIEWREQUESTPB = _descriptor.Descriptor(
  name='ImageViewRequestPb',
  full_name='ImageViewRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderID', full_name='ImageViewRequestPb.orderID', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=28,
  serialized_end=65,
)

DESCRIPTOR.message_types_by_name['ImageViewRequestPb'] = _IMAGEVIEWREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageViewRequestPb = _reflection.GeneratedProtocolMessageType('ImageViewRequestPb', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEVIEWREQUESTPB,
  '__module__' : 'ImageViewRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:ImageViewRequestPb)
  })
_sym_db.RegisterMessage(ImageViewRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
