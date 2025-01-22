
from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field


class RagEtlConfig(BaseSettings):
    """
    Configuration for RAG ETL processes
    """
    ETL_TYPE: str = Field(
        description="RAG ETL type ('luna' or 'Unstructured'), default to 'luna'",
        default="luna",
    )

    KEYWORD_DATA_SOURCE_TYPE: str = Field(
        description="Data source type for keyword extraction"
        " ('database' or other supported types), default to 'database'",
        default="database",
    )

    UNSTRUCTURED_API_URL: Optional[str] = Field(
        description="API URL for Unstructured.io service",
        default=None,
    )

    UNSTRUCTURED_API_KEY: Optional[str] = Field(
        description="API key for Unstructured.io service",
        default=None,
    )
