from pydantic import BaseModel
from typing import Optional


class ExtractSetting(BaseModel):
    datasource_type: str
    document_model: Optional[str] = None

    def __init__(self, **data) -> None:
        super().__init__(data)
