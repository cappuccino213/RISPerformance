# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ViOrderReportRequestPb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ViOrderReportRequestPb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1cViOrderReportRequestPb.proto\"\xd0\x0c\n\x16ViOrderReportRequestPb\x12\x15\n\rreviseEndDate\x18\x01 \x01(\t\x12\x0f\n\x07regDate\x18\x02 \x01(\t\x12\x1a\n\x12observationEndDate\x18\x03 \x01(\t\x12\x1a\n\x12preliminaryEndDate\x18\x04 \x01(\t\x12\x14\n\x0c\x61uditEndDate\x18\x05 \x01(\t\x12\x15\n\risFlimReading\x18\x06 \x01(\x08\x12\x15\n\rserviceSectID\x18\x07 \x01(\t\x12\x14\n\x0c\x65xamBodyPart\x18\x08 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssionNumber\x18\t \x01(\t\x12\x11\n\tpatientID\x18\n \x01(\t\x12\x13\n\x0binPatientNO\x18\x0b \x01(\t\x12\x14\n\x0cpatientClass\x18\x0c \x01(\t\x12 \n\x18pathologicalTrackingFlag\x18\r \x01(\t\x12\x16\n\x0eorganizationID\x18\x0e \x01(\t\x12\x0e\n\x06\x64\x65ptID\x18\x0f \x01(\t\x12\x14\n\x0c\x61\x62normalFlag\x18\x10 \x01(\t\x12\x19\n\x11retrospectiveFlag\x18\x11 \x01(\x08\x12\x14\n\x0cisOwnRepoert\x18\x12 \x01(\x08\x12\x0c\n\x04name\x18\x13 \x01(\t\x12\x16\n\x0e\x66ollowUpStatus\x18\x14 \x01(\x05\x12\x19\n\x11resultAssistantID\x18\x15 \x01(\t\x12\x12\n\nproviderID\x18\x16 \x01(\t\x12\x19\n\x11resultPrincipalID\x18\x17 \x01(\t\x12\x14\n\x0cresultStatus\x18\x18 \x01(\t\x12\x18\n\x10imagingDiagnosis\x18\x19 \x01(\t\x12\x19\n\x11pathologyDiagnose\x18\x1a \x01(\t\x12\x17\n\x0fpathologyRemark\x18\x1b \x01(\t\x12\x10\n\x08medrecNo\x18\x1c \x01(\t\x12\x14\n\x0coutPatientNO\x18\x1d \x01(\t\x12\x12\n\nphysicalNO\x18\x1e \x01(\t\x12\x13\n\x0binsuranceID\x18\x1f \x01(\t\x12\x13\n\x0b\x63urrentPage\x18  \x01(\x05\x12\x10\n\x08pageSize\x18! \x01(\x05\x12\x15\n\rqAachieveDate\x18\" \x01(\t\x12\x14\n\x0cnameLikeFlag\x18# \x01(\x08\x12\x0f\n\x07orderID\x18$ \x01(\t\x12\x19\n\x11observationDeptID\x18% \x01(\t\x12\x13\n\x0bprocedureID\x18& \x01(\t\x12\x15\n\rprocedureName\x18\' \x01(\t\x12\x1d\n\x15procedureNameLikeFlag\x18( \x01(\x08\x12\x1c\n\x14\x64iagnosisConsistency\x18) \x01(\x05\x12\x14\n\x0crequestOrgID\x18* \x01(\t\x12\x15\n\rrequestDeptID\x18+ \x01(\t\x12\x1e\n\x16isPathologicalTracking\x18, \x01(\x08\x12\x1d\n\x15isAuditDifferenceFlag\x18- \x01(\x08\x12\x10\n\x08\x63\x61seType\x18. \x01(\t\x12\x0b\n\x03sex\x18/ \x01(\t\x12\x10\n\x08\x61geArray\x18\x30 \x01(\t\x12\x0f\n\x07\x61geUnit\x18\x31 \x01(\t\x12\x11\n\tbirthDate\x18\x32 \x01(\t\x12\x16\n\x0enumberLikeFlag\x18\x33 \x01(\x08\x12\x1d\n\x15observationLocationID\x18\x34 \x01(\t\x12\x16\n\x0eresultReviseID\x18\x35 \x01(\t\x12\x14\n\x0cpreWritingID\x18\x36 \x01(\t\x12\x14\n\x0ctechnicianID\x18\x37 \x01(\t\x12\x19\n\x11\x64iagnosticGroupID\x18\x38 \x01(\t\x12\x0f\n\x07printed\x18\x39 \x01(\x08\x12\x0e\n\x06wardID\x18: \x01(\t\x12\r\n\x05\x62\x65\x64NO\x18; \x01(\t\x12\x14\n\x0cproviderName\x18< \x01(\t\x12\x1c\n\x14providerNameLikeFlag\x18= \x01(\x08\x12 \n\x18temporaryResultPrintFlag\x18> \x01(\x08\x12\x1b\n\x13\x66ollowUpStatusArray\x18? \x01(\t\x12\x15\n\rconsultStatus\x18@ \x01(\t\x12\x18\n\x10greenChannelFlag\x18\x41 \x01(\x08\x12\x11\n\tqueryType\x18\x42 \x01(\x05\x12\x10\n\x08pageType\x18\x43 \x01(\x05\x12\x15\n\risCheckedDate\x18\x44 \x01(\x08\x12\x0b\n\x03\x61ge\x18\x45 \x01(\x05\x12\x12\n\nqueryParam\x18\x46 \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_VIORDERREPORTREQUESTPB = _descriptor.Descriptor(
  name='ViOrderReportRequestPb',
  full_name='ViOrderReportRequestPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reviseEndDate', full_name='ViOrderReportRequestPb.reviseEndDate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regDate', full_name='ViOrderReportRequestPb.regDate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationEndDate', full_name='ViOrderReportRequestPb.observationEndDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preliminaryEndDate', full_name='ViOrderReportRequestPb.preliminaryEndDate', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auditEndDate', full_name='ViOrderReportRequestPb.auditEndDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isFlimReading', full_name='ViOrderReportRequestPb.isFlimReading', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='ViOrderReportRequestPb.serviceSectID', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examBodyPart', full_name='ViOrderReportRequestPb.examBodyPart', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accessionNumber', full_name='ViOrderReportRequestPb.accessionNumber', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientID', full_name='ViOrderReportRequestPb.patientID', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inPatientNO', full_name='ViOrderReportRequestPb.inPatientNO', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='patientClass', full_name='ViOrderReportRequestPb.patientClass', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathologicalTrackingFlag', full_name='ViOrderReportRequestPb.pathologicalTrackingFlag', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='organizationID', full_name='ViOrderReportRequestPb.organizationID', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deptID', full_name='ViOrderReportRequestPb.deptID', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abnormalFlag', full_name='ViOrderReportRequestPb.abnormalFlag', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retrospectiveFlag', full_name='ViOrderReportRequestPb.retrospectiveFlag', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isOwnRepoert', full_name='ViOrderReportRequestPb.isOwnRepoert', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='ViOrderReportRequestPb.name', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='followUpStatus', full_name='ViOrderReportRequestPb.followUpStatus', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultAssistantID', full_name='ViOrderReportRequestPb.resultAssistantID', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providerID', full_name='ViOrderReportRequestPb.providerID', index=21,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultPrincipalID', full_name='ViOrderReportRequestPb.resultPrincipalID', index=22,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultStatus', full_name='ViOrderReportRequestPb.resultStatus', index=23,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imagingDiagnosis', full_name='ViOrderReportRequestPb.imagingDiagnosis', index=24,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathologyDiagnose', full_name='ViOrderReportRequestPb.pathologyDiagnose', index=25,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pathologyRemark', full_name='ViOrderReportRequestPb.pathologyRemark', index=26,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medrecNo', full_name='ViOrderReportRequestPb.medrecNo', index=27,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outPatientNO', full_name='ViOrderReportRequestPb.outPatientNO', index=28,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='physicalNO', full_name='ViOrderReportRequestPb.physicalNO', index=29,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='insuranceID', full_name='ViOrderReportRequestPb.insuranceID', index=30,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currentPage', full_name='ViOrderReportRequestPb.currentPage', index=31,
      number=32, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageSize', full_name='ViOrderReportRequestPb.pageSize', index=32,
      number=33, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='qAachieveDate', full_name='ViOrderReportRequestPb.qAachieveDate', index=33,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nameLikeFlag', full_name='ViOrderReportRequestPb.nameLikeFlag', index=34,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderID', full_name='ViOrderReportRequestPb.orderID', index=35,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationDeptID', full_name='ViOrderReportRequestPb.observationDeptID', index=36,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procedureID', full_name='ViOrderReportRequestPb.procedureID', index=37,
      number=38, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procedureName', full_name='ViOrderReportRequestPb.procedureName', index=38,
      number=39, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procedureNameLikeFlag', full_name='ViOrderReportRequestPb.procedureNameLikeFlag', index=39,
      number=40, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diagnosisConsistency', full_name='ViOrderReportRequestPb.diagnosisConsistency', index=40,
      number=41, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestOrgID', full_name='ViOrderReportRequestPb.requestOrgID', index=41,
      number=42, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requestDeptID', full_name='ViOrderReportRequestPb.requestDeptID', index=42,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isPathologicalTracking', full_name='ViOrderReportRequestPb.isPathologicalTracking', index=43,
      number=44, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isAuditDifferenceFlag', full_name='ViOrderReportRequestPb.isAuditDifferenceFlag', index=44,
      number=45, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='caseType', full_name='ViOrderReportRequestPb.caseType', index=45,
      number=46, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sex', full_name='ViOrderReportRequestPb.sex', index=46,
      number=47, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ageArray', full_name='ViOrderReportRequestPb.ageArray', index=47,
      number=48, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ageUnit', full_name='ViOrderReportRequestPb.ageUnit', index=48,
      number=49, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='birthDate', full_name='ViOrderReportRequestPb.birthDate', index=49,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numberLikeFlag', full_name='ViOrderReportRequestPb.numberLikeFlag', index=50,
      number=51, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='observationLocationID', full_name='ViOrderReportRequestPb.observationLocationID', index=51,
      number=52, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resultReviseID', full_name='ViOrderReportRequestPb.resultReviseID', index=52,
      number=53, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preWritingID', full_name='ViOrderReportRequestPb.preWritingID', index=53,
      number=54, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='technicianID', full_name='ViOrderReportRequestPb.technicianID', index=54,
      number=55, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='diagnosticGroupID', full_name='ViOrderReportRequestPb.diagnosticGroupID', index=55,
      number=56, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='printed', full_name='ViOrderReportRequestPb.printed', index=56,
      number=57, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wardID', full_name='ViOrderReportRequestPb.wardID', index=57,
      number=58, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bedNO', full_name='ViOrderReportRequestPb.bedNO', index=58,
      number=59, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providerName', full_name='ViOrderReportRequestPb.providerName', index=59,
      number=60, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='providerNameLikeFlag', full_name='ViOrderReportRequestPb.providerNameLikeFlag', index=60,
      number=61, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temporaryResultPrintFlag', full_name='ViOrderReportRequestPb.temporaryResultPrintFlag', index=61,
      number=62, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='followUpStatusArray', full_name='ViOrderReportRequestPb.followUpStatusArray', index=62,
      number=63, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consultStatus', full_name='ViOrderReportRequestPb.consultStatus', index=63,
      number=64, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='greenChannelFlag', full_name='ViOrderReportRequestPb.greenChannelFlag', index=64,
      number=65, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryType', full_name='ViOrderReportRequestPb.queryType', index=65,
      number=66, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pageType', full_name='ViOrderReportRequestPb.pageType', index=66,
      number=67, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isCheckedDate', full_name='ViOrderReportRequestPb.isCheckedDate', index=67,
      number=68, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='ViOrderReportRequestPb.age', index=68,
      number=69, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='queryParam', full_name='ViOrderReportRequestPb.queryParam', index=69,
      number=70, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=1649,
)

DESCRIPTOR.message_types_by_name['ViOrderReportRequestPb'] = _VIORDERREPORTREQUESTPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ViOrderReportRequestPb = _reflection.GeneratedProtocolMessageType('ViOrderReportRequestPb', (_message.Message,), dict(
  DESCRIPTOR = _VIORDERREPORTREQUESTPB,
  __module__ = 'ViOrderReportRequestPb_pb2'
  # @@protoc_insertion_point(class_scope:ViOrderReportRequestPb)
  ))
_sym_db.RegisterMessage(ViOrderReportRequestPb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
