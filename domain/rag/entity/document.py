from pydantic import BaseModel, Field
from typing import Any, Optional


class Document(BaseModel):
    page_content: str
    metadata: Optional[dict] = Field(default_factory=dict)
    provider: Optional[str] = "luna"
