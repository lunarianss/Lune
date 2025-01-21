from config.option.minio_storage_config import MinioStorageConfig
from config.option.stroage_config import StorageConfig
from config.option.endpoint import EndpointConfig
from config.option.db import DatabaseConfig
from pydantic_settings import SettingsConfigDict


class LuneConfig(MinioStorageConfig, StorageConfig, EndpointConfig, DatabaseConfig):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", frozen=True, extra="ignore")
