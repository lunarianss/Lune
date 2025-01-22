from pydantic import BaseModel, ConfigDict
from typing import Optional


class UploadInfo(BaseModel):
    key: str
    tenant_id: str
    created_by: str

    def __init__(self, **data) -> None:
        super().__init__(**data)


class ExtractSetting(BaseModel):
    datasource_type: str
    document_model: Optional[str] = None
    upload_info: Optional[UploadInfo] = None
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __init__(self, **data) -> None:
        super().__init__(**data)
