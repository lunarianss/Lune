from pydantic import BaseModel, Field
from typing import Any, Optional


class Document(BaseModel):
    page_content: str
    vector: Optional[list[float]] = None
    metadata: Optional[dict] = Field(default_factory=dict)
    provider: Optional[str] = "luna"
