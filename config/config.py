from config.option.minio_storage_config import MinioStorageConfig
from pydantic_settings import SettingsConfigDict


class LuneConfig(MinioStorageConfig):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", frozen=True, extra="ignore")
