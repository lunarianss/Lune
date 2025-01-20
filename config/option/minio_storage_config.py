
from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import Field


class MinioStorageConfig(BaseSettings):
    MINIO_ENDPOINT: Optional[str] = Field(
        description="url of the minio endpoint", default=None)

    MINIO_BUCKET_NAME = Optional[str] = Field(
        description="bucket of the minio", default=None)

    MINIO_ACCESS_KEY: Optional[str] = Field(
        description="Access key ID for authenticating with the minio service",
        default=None,
    )

    MINIO_SECRET_KEY: Optional[str] = Field(
        description="Secret access key for authenticating with the minio service",
        default=None,
    )
    MINIO_USE_SSL: Optional[bool] = Field(
        description="Use https", default=False)
