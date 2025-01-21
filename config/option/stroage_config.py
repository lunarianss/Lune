
from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field


class StorageConfig(BaseSettings):
    STORAGE_TYPE: str = Field(
        description="Type of storage to use.",
        default="minio",
    )

    STORAGE_LOCAL_PATH: str = Field(
        description="Path for local storage when STORAGE_TYPE is set to 'local'.",
        default="storage",
    )
