from config.option.minio_storage_config import MinioStorageConfig
from config.option.stroage_config import StorageConfig
from config.option.endpoint import EndpointConfig
from config.option.db import DatabaseConfig
from config.option.rag_etl_config import RagEtlConfig
from pydantic_settings import SettingsConfigDict


class LuneConfig(MinioStorageConfig, StorageConfig, EndpointConfig, DatabaseConfig, RagEtlConfig):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", frozen=True, extra="ignore")
