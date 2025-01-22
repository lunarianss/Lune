from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExtractorRequest(_message.Message):
    __slots__ = ("upload_info", "process_rule_mode", "datasource_type", "document_model")
    UPLOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    PROCESS_RULE_MODE_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    upload_info: UploadInfo
    process_rule_mode: str
    datasource_type: str
    document_model: str
    def __init__(self, upload_info: _Optional[_Union[UploadInfo, _Mapping]] = ..., process_rule_mode: _Optional[str] = ..., datasource_type: _Optional[str] = ..., document_model: _Optional[str] = ...) -> None: ...

class UploadInfo(_message.Message):
    __slots__ = ("key", "tenant_id", "created_by")
    KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    key: str
    tenant_id: str
    created_by: str
    def __init__(self, key: _Optional[str] = ..., tenant_id: _Optional[str] = ..., created_by: _Optional[str] = ...) -> None: ...

class ExtractorReply(_message.Message):
    __slots__ = ("code", "msg", "documents")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    code: int
    msg: str
    documents: _containers.RepeatedCompositeFieldContainer[DocumentReply]
    def __init__(self, code: _Optional[int] = ..., msg: _Optional[str] = ..., documents: _Optional[_Iterable[_Union[DocumentReply, _Mapping]]] = ...) -> None: ...

class DocumentReply(_message.Message):
    __slots__ = ("page_content", "provider", "meta_data")
    class MetaDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PAGE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    page_content: str
    provider: str
    meta_data: _containers.ScalarMap[str, str]
    def __init__(self, page_content: _Optional[str] = ..., provider: _Optional[str] = ..., meta_data: _Optional[_Mapping[str, str]] = ...) -> None: ...
